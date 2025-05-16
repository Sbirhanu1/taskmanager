import unittest
from unittest.mock import patch
from io import StringIO
from task_manager import Task, add_task, view_tasks, mark_task_done, delete_task

class TestTaskManager(unittest.TestCase):
    def test_task_initialization(self):
        #Tests that Task attributes are correctly initialized
        task = Task("Test", "3", "2025-05-20")
        self.assertEqual(task.title, "Test")
        self.assertEqual(task.level, "3")
        self.assertEqual(task.deadline, "2025-05-20")
        self.assertFalse(task.is_done)

    def test_mark_done(self):
        #Tests that mark_done() correctly sets is_done to True
        task = Task("Test", "3", "2025-05-20")
        task.mark_done()
        self.assertTrue(task.is_done)

    def test_to_dict(self):
        #Tests that to_dict() returns correct dictionary representation of task
        task = Task("Test", "3", "2025-05-20", is_done=True)
        expected = {
            'Title': "Test",
            'Level': "3",
            'Deadline': "2025-05-20",
            'Completed': 'Yes'
        }
        self.assertEqual(task.to_dict(), expected)

    @patch('builtins.input', side_effect=["Test Task", "2", "2025-05-25"])
   
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task(self, mock_stdout, mock_input):
        #tests that add_task() correctly creates + appends a new task
        tasks = []
        add_task(tasks)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test Task")
        self.assertIn("Task added!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_tasks_empty(self, mock_stdout):
        #Test that view_tasks() correctly handles an empty task list
        view_tasks([])
        self.assertIn("No tasks to display", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_tasks_with_data(self, mock_stdout):
        #tests that the view_tasks() prints task details correctly
        tasks = [Task("Task 1", "1", "2025-05-20")]
        view_tasks(tasks)
        self.assertIn("Title: Task 1", mock_stdout.getvalue())

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=StringIO)
    def test_mark_task_done(self, mock_stdout, mock_input):
        #Tests that the mark_task_done() correctly marks the selected task as done
        task = Task("Do this", "2", "2025-05-30")
        tasks = [task]
        mark_task_done(tasks)
        self.assertTrue(task.is_done)
        self.assertIn("Task marked as done", mock_stdout.getvalue())

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_task(self, mock_stdout, mock_input):
        #tests that the delete_task() removes the selected task from the list
        tasks = [Task("Task to delete", "4", "2025-06-01")]
        delete_task(tasks)
        self.assertEqual(len(tasks), 0)
        self.assertIn("Task deleted", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
