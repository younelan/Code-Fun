def test_a():
  assert 'a'=='a'

class TestTwo:
  def setUp(self):
    global db,fp
    db = {'hello':'world'}
    with open('testlog.txt','a') as fp:
      fp.write('Logging from test\n')
     
  def tearDown(self):
    global db,fp
    db = {'hello':'world'}
    with open('testlog.txt','a') as fp:
      fp.write('Running teardown function\n')

  def test_two(self):
    assert 'b' == 'b'
