import os
import unittest
from helloworld import app

class TestCase(unittest.TestCase):

  def test_root(self):
    with app.test_client() as c:
      request = c.get('/')
      assert request.data.decode() == 'hello world'

  def test_root_upper_reverse(self):
    with app.test_client() as c:
      request = c.get('/?uppercase=true&reversed=true')
      assert request.data.decode() == 'DLROW OLLEH'
  
  def test_root_upper(self):
    with app.test_client() as c:
      request = c.get('/?uppercase=true')
      assert request.data.decode() == 'HELLO WORLD'

  def test_root_reverse(self):
    with app.test_client() as c:
      request = c.get('/?reversed=true')
      assert request.data.decode() == 'dlrow olleh'
  
  def test_hello(self):
    with app.test_client() as c:
      request = c.get('/hello')
      assert request.data.decode() == 'hello'

  def test_hello_upper_reverse(self):
    with app.test_client() as c:
      request = c.get('/hello?uppercase=true&reversed=true')
      assert request.data.decode() == 'OLLEH'
  
  def test_hello_upper(self):
    with app.test_client() as c:
      request = c.get('/hello?uppercase=true')
      assert request.data.decode() == 'HELLO'

  def test_hello_reverse(self):
    with app.test_client() as c:
      request = c.get('/hello?reversed=true')
      assert request.data.decode() == 'olleh'
  
  def test_world(self):
    with app.test_client() as c:
      request = c.get('/world')
      assert request.data.decode() == 'world'

  def test_world_upper_reverse(self):
    with app.test_client() as c:
      request = c.get('/world?uppercase=true&reversed=true')
      assert request.data.decode() == 'DLROW'
  
  def test_world_upper(self):
    with app.test_client() as c:
      request = c.get('/world?uppercase=true')
      assert request.data.decode() == 'WORLD'

  def test_world_reverse(self):
    with app.test_client() as c:
      request = c.get('/world?reversed=true')
      assert request.data.decode() == 'dlrow'

if __name__ == '__main__':
  unittest.main()
