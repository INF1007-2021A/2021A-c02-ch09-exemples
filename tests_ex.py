#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import inspect

from code_to_test import *


class MyTests(unittest.TestCase):
	def test_fibonacci_numbers_is_generator(self):
		self.assertTrue(
			inspect.isgeneratorfunction(fibonacci_numbers),
			"La fonction n'est pas un générateur"
		)

	def test_fibonacci_numbers_valid_lengths(self):
		# Catégories de valeurs pour length
		#	Valides:
		#		= 0
		#		= 1
		#		= 2
		#		> 2
		#	Invalides
		#		Pas un int
		#		= None
		#		< 0

		values = [
			0,
			1,
			2,
			5
		]
		expected = [
			[],
			[0],
			[0, 1],
			[0, 1, 1, 2, 3]
		]
		output = [[fibo for fibo in fibonacci_numbers(v)] for v in values]
		
		self.assertListEqual(
			output,
			expected
		)

	def test_fibonacci_numbers_invalid_lengths(self):
		values = [
			"henlo",
			None,
			-42
		]
		expected_except = [
			TypeError,
			TypeError,
			ValueError
		]

		for v, e in zip(values, expected_except):
			with self.assertRaises(e):
				fibo_series = [fibo for fibo in fibonacci_numbers(v)]

	def test_build_recursive_sequence_generator(self):
		def fibo_def(last_elems):
			return last_elems[-1] + last_elems[-2]
		fibo = None
		try:
			fibo = build_recursive_sequence_generator([0, 1], fibo_def, False)
		except:
			self.fail("l'appel échoue")
		self.assertTrue(
			inspect.isgeneratorfunction(fibo),
			"L'objet retourné n'est pas un générateur"
		)
		values = [
			1,
			2,
			5,
			10
		]
		expected = [
			[0],
			[0, 1],
			[0, 1, 1, 2, 3],
			[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
		]
		output = [[fib for fib in fibo(v)] for v in values]
		self.assertListEqual(
			output,
			expected
		)


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
