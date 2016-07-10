namespace ButterflyRecognition
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.OpenImg = new System.Windows.Forms.Button();
            this.Result = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(337, 259);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // OpenImg
            // 
            this.OpenImg.Location = new System.Drawing.Point(355, 12);
            this.OpenImg.Name = "OpenImg";
            this.OpenImg.Size = new System.Drawing.Size(75, 23);
            this.OpenImg.TabIndex = 1;
            this.OpenImg.Text = "Open image";
            this.OpenImg.UseVisualStyleBackColor = true;
            this.OpenImg.Click += new System.EventHandler(this.OpenImg_Click);
            // 
            // Result
            // 
            this.Result.Location = new System.Drawing.Point(355, 41);
            this.Result.Name = "Result";
            this.Result.Size = new System.Drawing.Size(236, 20);
            this.Result.TabIndex = 3;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(630, 310);
            this.Controls.Add(this.Result);
            this.Controls.Add(this.OpenImg);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button OpenImg;
        private System.Windows.Forms.TextBox Result;
    }
}

