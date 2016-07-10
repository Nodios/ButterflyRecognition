using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;

namespace ButterflyRecognition
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void OpenImg_Click(object sender, EventArgs e)
        {
            string OpenImage;
            OpenFileDialog FileDialog = new OpenFileDialog();
            FileDialog.Filter = "jpg files (*.jpg) |*.jpg";
            if(FileDialog.ShowDialog() == DialogResult.OK)
            {
                OpenImage = FileDialog.FileName;
                Bitmap image = new Bitmap(OpenImage, true);
                pictureBox1.Image = image;
                pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            }
            // full path of python interpreter 
            string python = @"C:\Users\Josip\Desktop\WinPython-64bit-3.4.4.2\python-3.4.4.amd64\python.exe";

            // python app to call 
            string myPythonApp = "C:\\Users\\Josip\\Desktop\\ButterflyRecognition-master\\azureWebService.py";

            // Create new process start info 
            ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python);

            // make sure we can read the output from stdout 
            myProcessStartInfo.UseShellExecute = false;
            myProcessStartInfo.RedirectStandardOutput = true;

            myProcessStartInfo.Arguments = myPythonApp;

            Process myProcess = new Process();
            // assign start information to the process 
            myProcess.StartInfo = myProcessStartInfo;

            // start the process 
            myProcess.Start();

            // Read the standard output of the app we called.  
            // in order to avoid deadlock we will read output first 
            // and then wait for process terminate: 
            StreamReader myStreamReader = myProcess.StandardOutput;
            string myString = myStreamReader.ReadLine();

            /*if you need to read multiple lines, you might use: 
                string myString = myStreamReader.ReadToEnd() */

            // wait exit signal from the app we called and then close it. 
            myProcess.WaitForExit();
            myProcess.Close();

            Result.Text = myString;
        }
    }
}
