from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team, self.team)

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.user, type='Running', duration=30)
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.duration, 30)

    def test_workout_creation(self):
        workout = Workout.objects.create(user=self.user, name='Morning Cardio', description='Cardio session')
        self.assertEqual(workout.name, 'Morning Cardio')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team=self.team, points=100)
        self.assertEqual(leaderboard.points, 100)
