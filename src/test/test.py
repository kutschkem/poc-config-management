import unittest
import vagrant
import os
import subprocess

class test_provisioning(unittest.TestCase):

    def test_provisioning(self):
        root = os.path.join(os.path.dirname(__file__),'..','vagrant')
        v = vagrant.Vagrant(root=root)
        v.up()
        try:
            cmd = ["vagrant", "ssh", "-c", "test -f hello_world"]
            p = subprocess.Popen(cmd, cwd=root)
            p.communicate()
            if p.returncode != 0:
                raise Exception("File not found: hello_world")
        finally:
            v.destroy()

if __name__=="__main__":
    unittest.main()
