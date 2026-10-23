import json
import os
import tempfile
import unittest

import app as hj


class HackJudgeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        hj.DB_PATH = os.path.join(self.tmp.name, "test.db")
        hj.init_db()
        self.client = hj.app.test_client()

    def tearDown(self):
        self.tmp.cleanup()

    def test_health_and_empty_list(self):
        self.assertEqual(self.client.get('/api/health').status_code, 200)
        self.assertEqual(self.client.get('/api/hackathons').json, [])

    def test_create_hackathon_requires_weights_total_100(self):
        payload = {"name": "Test", "criteria": [{"name": "Build", "description": "Quality", "weight": 40}]}
        response = self.client.post('/api/hackathons', json=payload)
        self.assertEqual(response.status_code, 400)
        payload["criteria"] = [{"name": "Build", "description": "Quality", "weight": 100}]
        response = self.client.post('/api/hackathons', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["criteria"][0]["weight"], 100)

    def test_override_requires_reason_and_records_audit(self):
        h = self.client.post('/api/hackathons', json={"name":"Test", "criteria":[{"name":"Build","description":"Quality","weight":100}]}).json
        with hj.db() as con:
            cur = con.execute("INSERT INTO submissions(hackathon_id,team_name,project_name,github_url,status,score,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?)", (h['id'], 'Team', 'App', 'https://github.com/example/app', 'EVALUATED', 65.0, hj.now_iso(), hj.now_iso()))
            sid = cur.lastrowid
        bad = self.client.post(f'/api/submissions/{sid}/override', json={"score":80})
        self.assertEqual(bad.status_code, 400)
        good = self.client.post(f'/api/submissions/{sid}/override', json={"score":82.5,"reason":"Human review found additional evidence"})
        self.assertEqual(good.status_code, 200)
        self.assertEqual(good.json['score'], 82.5)
        detail = self.client.get(f'/api/submissions/{sid}').json
        self.assertEqual(detail['audit_log'][0]['action'], 'score_override')

    def test_github_url_validation(self):
        with self.assertRaises(ValueError):
            hj.github_repo_from_url('https://evil.example/github.com/owner/repo')
        self.assertEqual(hj.github_repo_from_url('https://github.com/owner/repo.git'), ('owner','repo'))


if __name__ == '__main__':
    unittest.main()
