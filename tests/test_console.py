#!/usr/bin/python3
"""Test suite for the console (command interpreter)"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand  # Import your console class


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

    def test_create(self):
        """Test create command with a valid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            self.assertRegex(output, r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')

    def test_create_invalid_class(self):
        """Test create command with an invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create InvalidClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show(self):
        """Test show command with a valid class and id"""
        with patch('sys.stdout', new=StringIO()) as f:
            # Create a user first
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            
            # Try to show the created user
            f.seek(0)
            f.truncate(0)
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn(user_id, output)

    def test_show_missing_id(self):
        """Test show command with a missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy(self):
        """Test destroy command with a valid class and id"""
        with patch('sys.stdout', new=StringIO()) as f:
            # Create a user first
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            
            # Destroy the created user
            f.seek(0)
            f.truncate(0)
            HBNBCommand().onecmd(f"destroy User {user_id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "")
            
            # Try to show the destroyed user
            f.seek(0)
            f.truncate(0)
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        """Test all command with valid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            f.seek(0)
            f.truncate(0)
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn("User", output)

    def test_all_invalid_class(self):
        """Test all command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all InvalidClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


if __name__ == "__main__":
    unittest.main()
