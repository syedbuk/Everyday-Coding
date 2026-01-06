import inquirer from 'inquirer';
import qr from 'qr-image';
import x from 'fs';



inquirer.prompt([
  {
    message: 'What is your name?',
    name: 'URL',
  }.then(answers => {
    const url = answers.URL;
    const qr_svg = qr.image(url);
    qr_svg.pipe(x.createWriteStream('qrcode.png'));
  })
  .catch((err)=>{

    if (err){
    console.error(err);
  } else {
    
    console.log("QR Code generated!");
  }

    })



