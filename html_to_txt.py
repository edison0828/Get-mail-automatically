from bs4 import BeautifulSoup
import re

def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Function to extract text from tags
    def extract_text(tag):
        return tag.get_text(separator="\n").strip()
    
    # Extract title
    title = soup.title.string if soup.title else "无标题"

    # Extract all headings
    headings = []
    for i in range(1, 7):
        for header in soup.find_all(f'h{i}'):
            headings.append(f"{'#' * i} {extract_text(header)}")

    # Extract all paragraphs
    paragraphs = [extract_text(p) for p in soup.find_all('p')]

    # Extract all links
    links = [f"[{extract_text(a)}]({a['href']})" for a in soup.find_all('a', href=True)]

    # Extract all images
    images = [f"![{img.get('alt', '图片')}]({img['src']})" for img in soup.find_all('img', src=True)]

    # Combine extracted text
    combined_text = "\n\n".join(headings + paragraphs + links + images)
    
    # Clean up extra whitespace
    combined_text = re.sub(r'\n{3,}', '\n\n', combined_text)
    
    return f"# {title}\n\n{combined_text}".strip()

def write_to_markdown_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

# Example HTML content
html_content = """
<!doctype html>

<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<meta name="viewport" content="width=device-width">

<!--[if !mso]><!-- -->

<meta http-equiv="X-UA-Compatible" content="IE=edge">

<!--<![endif]-->

<!--[if gte mso 9]><xml>

<o:OfficeDocumentSettings>

<o:AllowPNG/>

<o:PixelsPerInch>96</o:PixelsPerInch>

</o:OfficeDocumentSettings>

</xml><![endif]-->



<style>



@media only screen and (min-width: 650px) {

	.p13_mm_offer_tag{font-size:14px!important;line-height:22px!important;}

	.p13_mm_discounted_price{font-size:16px!important;line-height:22px!important;}

	.p13_mm_original_price{font-size:14px!important;line-height:22px!important;}

	.p13_mm_description{font-size:14px!important;line-height:22px!important;}

}





@media only screen and (max-width: 430px){

  .temp_td_h5{ font-size: 16px !important; line-height: 22px !important;  }

  .temp_display_table{display:table !important;}

  .temp_mob_reset{padding:0!important;}

}



  

</style>



<style type="text/css">

@media only screen and (max-width: 640px){

	.left_aligned{text-align:left!important;}

	.mob_h_130{height:130px!important;}

}

  

@media only screen and (max-width: 350px){

	.mob_h_73{height:73px!important;}

}



</style>



<style type="text/css">

a {text-decoration: none;}

a[x-apple-data-detectors] { color: inherit !important; text-decoration: none !important; font-size: inherit !important; font-family: inherit !important; font-weight: inherit !important; line-height: inherit !important } table{ mso-table-lspace: 0; mso-table-rspace: 0; mso-table-lspace: 0; border: none; border-collapse: collapse; border-spacing: 0;} p {margin: 0 !important;} h1, .h1, .h1l{ font-size: 60px !important; line-height: 66px !important; } .h1xl{ font-size: 108px !important; line-height: 108px !important; } .hsubxl {font-size: 28px !important; line-height: 36px !important; font-family: 'Uber Move', 'Helvetica Neue', Helvetica, Arial, sans-serif !important; font-weight: 500 !important; } .h1bl { font-size: 50px !important; line-height: 54px !important; } h2, .h2, .h2l { font-size: 44px !important; line-height: 50px !important; } ul, ol {padding-left:0; margin:0; margin-left:30px !important;} u + .body ul, u + .body ol { margin-left: 30px !important; } 



@media only screen and (max-width: 640px) { u + .body ul, u + .body ol { margin-left: 18px !important;} }

.show670, .show414 {display:none;} 



@media screen and (max-width:670px) { .t1of12, .t2of12, .t3of12, .t4of12, .t5of12, .t6of12, .t7of12, .t8of12, .t9of12, .t10of12, .t11of12, .t12of12, .full { width: 100% !important; max-width: none !important; } .show670 { display: block !important; max-height: none !important; overflow:visible !important; } .mobheight0{height:0 !important; line-height: 0 !important;} .hide670 { display: none !important; } .mobheightAuto{height:auto !important;} } 



@media screen and (min-width:671px) { .force700{width: 700px !important;} .desktar {text-align: right !important;} } 





@media screen and (max-width:430px) { h1, h2, .h1, .h1l, .h2{ font-size: 34px !important; line-height: 40px !important;} .h1xl{ font-size: 70px !important; line-height: 70px !important;} .h1scale, .h1lscale {font-size: 54px !important; line-height: 60px !important;} .h2scale, .h2lscale {font-size: 42px !important; line-height: 48px !important;} .hsubxl {font-size: 24px !important; line-height: 30px !important; font-family: 'Uber Move', 'Helvetica Neue', Helvetica, Arial, sans-serif !important; font-weight: 500 !important;} .h1bl { font-size: 22px !important; line-height: 28px !important; } .p1scale{font-size: 16px !important;line-height: 22px !important;} .show414 { display: block !important; max-height: none !important; overflow:visible !important; } .hide414 { display: none !important; } } 



@media screen and (max-width:375px) { .h1xl{ font-size: 70px !important; line-height: 70px !important;} .hsubxl { font-size: 20px !important; line-height: 26px !important; font-family: 'Uber Move Text', 'Helvetica Neue', Helvetica, Arial, sans-serif  !important; font-weight: 700 !important; } .h1scale {font-size: 46px !important; line-height: 52px !important;} .h2scale {font-size: 40px !important; line-height: 46px !important;} }





@font-face{font-family: 'UberMove-Medium'; src: url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMove-Medium.woff') format('woff'), url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMove-Medium.ttf') format('truetype'); font-weight: normal !important; font-style: normal !important; mso-font-alt: 'Arial'}@font-face{font-family: 'UberMoveText-Regular'; src: url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Regular.woff') format('woff'), url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Regular.ttf') format('truetype'); font-weight: normal !important; font-style: normal !important; mso-font-alt: 'Arial'}

@font-face{font-family: 'UberMoveText-Medium'; src: url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Medium.woff') format('woff'), url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Medium.ttf') format('truetype'); font-weight: normal !important; font-style: normal !important; mso-font-alt: 'Arial'}@font-face{font-family: 'UberMoveText-Bold'; src: url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Bold.woff') format('woff'), url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Bold.ttf') format('truetype'); font-weight: normal !important; font-style: normal !important; mso-font-alt: 'Arial'}

@font-face{font-family: 'Uber Move Text'; src: url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Bold.woff') format('woff'), url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Bold.ttf') format('truetype'); font-weight: bold; mso-font-alt: 'Arial'}@font-face{font-family: 'Uber Move Text'; src: url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Medium.woff') format('woff'), url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Medium.ttf') format('truetype'); font-weight: 500; mso-font-alt: 'Arial'}

@font-face{font-family: 'Uber Move Text'; src: url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Regular.woff') format('woff'), url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMoveText-Regular.ttf') format('truetype'); font-weight: normal; mso-font-alt: 'Arial'}@font-face{font-family: 'Uber Move'; src: url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMove-Medium.woff') format('woff'), url('https://d3smpkehiq8afm.cloudfront.net/assets/fonts/UberMove/UberMove-Medium.ttf') format('truetype'); font-weight: 500; mso-font-alt: 'Arial'}

sup { line-height:0; font-size:70%; }  

</style>

















<style>

sup { line-height:0; font-size:70%; }



  

 @media screen and (max-width:414px) {

	.mobilebgcolor{

      background-color: #00ff00 !important;

   }

     .hide {display: none !important;}

  .show {display: inline-block !important; width:auto !important; height:auto !important; overflow:visible !important; float:none !important; visibility:visible !important; border:none !important; padding-bottom:0px !important; vertical-align: bottom !important;}

  .show1 {

    display: block !important;

    max-height: none !important;

  }

  .mobh1 {font-size: 44px !important; line-height: 50px !important;}

  .mobh2 {font-size: 34px !important;line-height: 40px !important;}  

 .p3mob {font-size:14px !important; line-height: 20px !important}

 .h5mob{font-size: 24px !important; line-height:30px !important}

  .h2m {font-size: 36px !important; line-height: 42px !important}

  .width33 { max-width: 33% !important; width: 33% !important}

  .width34 {max-width: 34% !important; max-width: 34% !important; }



  

}





  

</style>  

</head>

<body class="body" dir=ltr style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background-color:#d6d6d5;margin:0;min-width:100%;padding:0;width:100%">

<span id="Preheader" class="preheader" data-blockuuid="9629310d-067d-4bc0-bd13-0291ec686aa1" style="display: none; max-height: 0px; font-size: 0px; overflow: hidden; mso-hide: all;">

只到本月！下單完成任務抽最高 200 點💰

&#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy;

&#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy;

&#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy;

&#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy;

&#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy;

&#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy;

&#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &#847; &shy;



</span>

<span id="TemplateUUID_cdea035a-8190-42b6-9321-25680ad0c3bb"></span>

  

<span id="WorkflowUUID_286a8c55-c241-44aa-975c-6d41cb07fe26"></span>   



<style>.yahooHide{display:none!important}</style>

<table width="100%" border="0" cellpadding="0" cellspacing="0" style="background-color:#d6d6d5;border:0;border-collapse:collapse;border-spacing:0;" bgcolor="#d6d6d5" class="">

<tbody>

<tr>

<td align="center" style="display: block;">

<!--[if (gte mso 9)|(IE)]>

<table width="700" align="center" cellpadding="0" cellspacing="0" border="0">

<tr>

<td>

<![endif]-->

<table width="100%" border="0" cellpadding="0" cellspacing="0" style="border:0;border-collapse:collapse;border-spacing:0;max-width:700px;" class="force700">

<tbody>

<tr>

<td style="background-color:#ffffff">





































   

   

   

   



  









        

    













   

   









    





















<table width="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%;" data-blockuuid="7e833e5e-168b-4a3b-bef3-1d232ed565c9">





<!--  Header  center logo  -->



   <tbody>

      <tr>

      <td class="outsidegutter" align="left" style="direction:ltr;text-align:left;padding: 0 14px 0 14px; background-color: #ffffff;" background="https://d3smpkehiq8afm.cloudfront.net/assets/Logos/dark_mode_background/darkmode_BG_white.jpg">

         <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%;">

            <tbody>

               <tr>

               <td style="direction:ltr;text-align:left; padding-top: 10px; padding-bottom: 10px;">

<!--[if (gte mso 9)|(IE)]>

<table width="560" align="center" cellpadding="0" cellspacing="0" border="0">

   <tr>

      <td>

         <![endif]-->

         <table border="0" cellpadding="0" cellspacing="0" class="t10of12" align="center" style="Margin: 0 auto; border-collapse: collapse; max-width: 560px; width: 100%;">

            <tbody><tr>

               <td style="direction:ltr;text-align:left;padding-left: 12px; padding-right: 12px; vertical-align: middle;">

                  <table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="border-collapse: collapse; table-layout: fixed; width: 100%;">

                     <tbody><tr>

                        <td style="direction:ltr;text-align:left; height:54px; text-align: center; font-size:0; line-height: 0;">







<!-- E A T S H - - - - - - -->

   

   <a href="http://email.uber.com/ss/c/u001.3rz4IfclD0-2ph6Eff9d63g_dErgruABBRYcWl3Pm2lALawWvX-yC6XWR8qGvsgO/47c/bwGpxaGZT4GyP2v76A_9_Q/h0/h001.dQ4EokQjGAEfcFsdT52qqi0xukSnXkHLD_zZ268hobQ" style="text-decoration: none; display:inline-block;">

   <img src="https://d3smpkehiq8afm.cloudfront.net/assets/Logos/Eats/rebrand/eats-logoh-147x43_2x_allblack.png" width="147" height="43" style="-ms-interpolation-mode: bicubic; clear: both; display: block; max-width: 100%; outline: none; text-decoration: none;"  alt="Uber Eats">

   </a>

   













                        </td>

                     </tr>

                  </tbody></table>

               </td>

            </tr>

         </tbody></table>

         <!--[if (gte mso 9)|(IE)]>

      </td>

   </tr>

</table>

<![endif]-->

               </td>

            </tr>

         </tbody></table>

      </td>

   </tr>

</tbody>

<!--  close Header center logo  -->



























</table>













































   

   

































	

	

	

		













<!--  HB_BANNER 4.0 cf 4/15/22  -->

<table width="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%;" data-blockuuid="36f8110c-cdc7-4f6c-a85e-0a9ac4a9d52e">

<tbody>

<tr>

<td style="background-color:#06C167; padding-top: 0px; padding-bottom: 0px;">

<table border="0" cellpadding="0" cellspacing="0" style="width: 100%;" class="">



<tr>

<td class="" align="left" style="direction:ltr;text-align:left;">

<div class="hide414">



<img src="https://d1g1f25tn8m2e6.cloudfront.net/7ca0c876-4336-4ae1-a9e8-69a51c5de23e.png" width="700" height="" style="-ms-interpolation-mode: bicubic; clear: both; display: block; height: auto; max-width: 700px; outline: none; text-decoration: none; width: 100%;  color:#000000;" border="0" alt="">  

</div>

<!--[if !mso 9]><!--><div class="show414" style="mso-hide:all;display:none;max-height:0px;overflow:hidden;">



<img src="https://d1g1f25tn8m2e6.cloudfront.net/7713260a-8761-4e75-80ad-7b903fa17838.png" width="414" height="" style="-ms-interpolation-mode: bicubic; clear: both; display: block; height: auto; max-width: 414px; outline: none; text-decoration: none; width: 100%;  color:#000000;" border="0" alt="">  

</div><!--<![endif]-->

</td>

</tr>



</table>

</td>

</tr>

</tbody></table>

<!--  END BG CROP + SCALE  -->



<table width="100%" border="0" cellpadding="0" cellspacing="0" style="border:0;border-collapse:collapse;border-spacing:0;margin:auto;max-width:700px;" class="">

<tbody>

<tr>

<td align="center">

<table width="100%" border="0" cellpadding="0" cellspacing="0" style="background-color:#fff;border:0;border-collapse:collapse;border-spacing:0;margin:auto;" bgcolor="#ffffff" class="basetable">

<tbody>

<tr>

<td align="center">

<!--[if (gte mso 9)|(IE)]>

<table width="700" align="center" cellpadding="0" cellspacing="0" border="0">

<tr>

<td align="center">

<![endif]-->

<table width="100%" border="0" cellpadding="0" cellspacing="0" class="basetable" style="border:0;border-collapse:collapse;border-spacing:0;">

<tbody>

<tr>

<td align="center" style="background-color:#ffffff">

<table border="0" cellpadding="0" cellspacing="0" width="100%" class="basetable" style="border:0;border-collapse:collapse;border-spacing:0;">

<tbody>

<tr>

<td>

<!--[if (gte mso 9)|(IE)]>

<table width="100%" align="center" cellpadding="0" cellspacing="0" border="0">

<tr>

<td>

<![endif]-->

<table width="100%" border="0" cellpadding="0" cellspacing="0" class="basetable" style="border:0;border-collapse:collapse;border-spacing:0;">

<tbody>

<tr>

<td>

<!--[if (gte mso 9)|(IE)]>

<table width="100%" align="center" cellpadding="0" cellspacing="0" border="0">

<tr>

<td>

<![endif]-->

<table width="100%" border="0" cellpadding="0" cellspacing="0" style="border:0;border-collapse:collapse;border-spacing:0;" class="">

<tbody>

<tr>

<td>

















































































































































<table border="0" cellpadding="0" cellspacing="0"

style="border-collapse:collapse;width:100%;direction:ltr;" role="presentation"

bgcolor="#ffffff" data-blockuuid="88854ba2-7046-4717-93a0-a0f1116d874b">

<tr>

<td class="outsidegutter" align="left"

style="direction:ltr;text-align:left; padding-left: 14px; padding-right: 14px;">

<table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%;"

role="presentation">

<tr>

<td style="direction:ltr;text-align:left;">

<!--[if (gte mso 9)|(IE)]>

<table align="center" cellpadding="0" cellspacing="0" border="0"

role="presentation" style="width:560px;">

<tr>

<td>

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t10of12" align="center"

style="Margin: 0 auto; border-collapse: collapse; max-width: 560px; width: 100%;"

role="presentation">

<tr>

<td style="direction:ltr;text-align:left;">

<table border="0" cellpadding="0" cellspacing="0" width="100%"

align="left"

style="border-collapse: collapse; table-layout: fixed; width: 100%;"

role="presentation">



<tr>

<td height="50"

style="font-size:50px;line-height:50px;mso-line-height-rule:exactly;opacity:0;#ffffff;">

&nbsp;

</td>

</tr>



<tr>



<td

style="direction:ltr;text-align:left;padding:0px 12px 0px 12px;">

<h4

class="" style="Margin:0;

padding:0;mso-line-height-rule:exactly;

font-family:'Uber Move','HelveticaNeue',

Helvetica,Arial,sans-serif;

font-size: 28px; line-height: 34px;

font-weight: 500; color:

#000000;">

<a

href="http://email.uber.com/ss/c/u001.mspHjJOk8JIj3l-SrEEc6bs4Hzdu2xbFIYVS-8V0AO4DOtso8EEdzAt5iBsmiVff/47c/bwGpxaGZT4GyP2v76A_9_Q/h1/h001.YwjHHD-Q5CHVLVbm6mUgJrnfI4VfvwSSh8LVoyXyr_Y"

style="text-decoration:none;#000000;"><strong

style="color:#000000;text-decoration:none;font-weight:500;direction:ltr;">

超賺回饋最後倒數 ⏰ 享回饋，就用 LINE Pay！



</strong></a>

</h4>

</td>



</tr>



<tr>

<td class="p2"

style="direction:ltr;text-align:left;color:#000000;font-family:'Uber Move Text','HelveticaNeue',Helvetica,Arial,sans-serif;font-size: 16px;font-weight:normal;line-height: 22px;padding-left:12px;padding-right:12px;padding-bottom:20px;padding-top:10px;">

<a

href="http://email.uber.com/ss/c/u001.mspHjJOk8JIj3l-SrEEc6bs4Hzdu2xbFIYVS-8V0AO4DOtso8EEdzAt5iBsmiVff/47c/bwGpxaGZT4GyP2v76A_9_Q/h2/h001._EQHCAd-7MTuxG3-ID1KJ4sbxms1h8P-IiFNe2HtCpo"

style="text-decoration:none;color:#000000;"><strong

style="color:#000000;text-decoration:none;font-weight:normal;direction:ltr;">



</strong></a>

</td>

</tr>





<tr>

<td

style="direction:ltr;text-align:left; padding-left: 12px; padding-right: 12px; padding-bottom: 30px; ">

<table border="0" cellpadding="0" cellspacing="0" class="basetable" width="100%" align="left" style="table-layout: fixed; width: 100%;" role="presentation">

<tr>

<td class="cta" lang="x-textcta" style="direction:ltr;text-align:left;font-family: 'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 700; line-height: 22px;">



<a href="http://email.uber.com/ss/c/u001.mspHjJOk8JIj3l-SrEEc6bs4Hzdu2xbFIYVS-8V0AO4DOtso8EEdzAt5iBsmiVff/47c/bwGpxaGZT4GyP2v76A_9_Q/h3/h001.cRh6rrGCfZLgSLCrbLVsu35sX7tHjG9-tPc9--FivMY"

style="text-decoration:none; color: #000000;"><strong

style="color: #000000; text-decoration: none; font-weight: 700; direction: ltr;">完整活動說明請點此&nbsp;&nbsp;&gt;</strong></a>



</td>

</tr>

</table>

</td>

</tr>



<tr>

<td style="direction:ltr;text-align:left;">

<table border="0" cellpadding="0" cellspacing="0" width="100%"

align="left"

style="border-collapse: collapse; table-layout: fixed; width: 100%;"

role="presentation">





































































































































































































































































<!--[if !mso 9]><!-->

<head>

<style type="text/css">

@media screen and (min-width:671px) {

.outlook-mac-fix-left .floatleft {

float: left !important

}

.outlook-mac-fix-right .floatright {

float: right !important

}

}

@media screen and (max-width:430px) {

.heightauto {

height: auto !important

}

.pt20 {

padding-top: 20px !important;

}

.pr20 {

padding-right: 20px !important;

}

.pl20 {

padding-left: 20px !important;

}

.floatleft {

float: left !important;

}

.floatright {

float: right !important;

}

}

</style>

</head>

<!--<![endif]-->









<tr data-blockuuid="91c2cdd0-daac-483d-8434-b45bf7f8105b">

<td style="font-size:1px;line-height:1px;vertical-align:top;padding-left:12px;padding-right:12px;"

valign="top" align="left">

<!--[if (gte mso 9)|(IE)]>

<table align="left" cellpadding="0" cellspacing="0" border="0" role="presentation"

style="width:536px;">

<tr>

<td width="536">

<![endif]-->

<table width="536" border="0" cellspacing="0" cellpadding="0" align="left"

role="presentation"

style="width:100%;max-width:536px;direction:ltr;text-align:left;">



<tr>

<td style="font-size:1px;line-height:1px;border-radius:10px;" bgcolor="#d3efda"

align="left">

<table style="width:100%;border-radius:10px;" cellpadding="0" cellspacing="0" border="0"

align="left" role="presentation">

<tr>

<td style="font-size:1px;line-height:1px;vertical-align:middle;border-radius:10px;"

valign="middle" align="left">

<!--[if (gte mso 9)|(IE)]>

<table align="left" cellpadding="0" cellspacing="0"

border="0" role="presentation" style="width:536px;">

<tr>

<td width="536">

<![endif]-->

<table border="0" cellspacing="0" cellpadding="0"

align="left"

style="width:100%;max-width:536px;vertical-align:middle;"

role="presentation">

<tr>

<td style="vertical-align:middle;" valign="middle">

<!--[if (gte mso 9)|(IE)]>

<table align="left"

cellpadding="0" cellspacing="0" border="0"

role="presentation"

style="width:238px;direction:ltr;vertical-align:middle;">

<tr>

<td width="238"

style="font-size:1px;line-height:1px;vertical-align:middle;"

align="left">

<![endif]-->

<table border="0" cellspacing="0"

cellpadding="0"

align="left"

role="presentation"

style="width:100%;max-width:238px;direction:ltr;vertical-align:middle;float:left;"

class="full floatleft outlook-mac-fix-left">

<tr>

<td style="font-size:1px;line-height:1px;vertical-align:middle;"

valign="middle"

align="left"

height="278"

class="heightauto">

<table

width="218"

border="0"

cellspacing="0"

cellpadding="0"

align="left"

role="presentation"

style="direction:ltr;text-align:left;width:100%;max-width:430px;vertical-align:middle;">

<tr>

<td style="direction:ltr;text-align:left;padding-left:20px;padding-top:30px;padding-bottom:30px;vertical-align:middle;"

align="left"

valign="middle"

class="hide414">



<img src="https://d1g1f25tn8m2e6.cloudfront.net/df05f855-e4de-4554-a978-a3818d024812.png"

alt="LINE Points"

title="LINE Points"

width="218"

height="218"

border="0"

style="vertical-align:middle;display:inline-block!important;font-family:'Uber Move','HelveticaNeue',Helvetica,Arial,sans-serif;font-size:14px;line-height:17px;color:#000000;font-weight:500;text-decoration:none;width:100%;max-width:238px;height:218px;" />



</td>

<!--[if !mso 9]><!-->

<td style="direction:ltr;text-align:left;padding-left:20px;padding-right:20px;padding-top:30px;;vertical-align:middle;display:none;overflow:hidden;max-height:0;mso-hide:all;"

align="left"

valign="middle"

class="show414">



<img src="https://d1g1f25tn8m2e6.cloudfront.net/df05f855-e4de-4554-a978-a3818d024812.png"

alt="LINE Points"

title="LINE Points"

width="218"

height="218"

border="0"

style="vertical-align:middle;display:inline-block!important;font-family:'Uber Move','HelveticaNeue',Helvetica,Arial,sans-serif;font-size:14px;line-height:17px;color:#000000;font-weight:500;text-decoration:none;width:100%;max-width:218px;height:auto;" />



</td>

<!--<![endif]-->

</tr>

</table>

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

<td width="298"

style="font-size:1px;line-height:1px;"

align="center">

<![endif]-->

<table border="0" cellspacing="0"

cellpadding="0" align="center"

style="width:100%;max-width:298px;float:right;"

role="presentation"

class="full floatright outlook-mac-fix-right">

<tr>

<td style="font-size:1px;line-height:1px;vertical-align:middle;"

valign="middle"

align="left"

height="278"

class="heightauto">

<!--[if (gte mso 9)|(IE)]>

<table

align="left"

cellpadding="0"

cellspacing="0"

border="0"

role="presentation"

style="width:298px;">

<tr>

<td

width="298">

<![endif]-->

<table

border="0"

cellspacing="0"

cellpadding="0"

align="center"

style="width:100%;max-width:298px;"

role="presentation"

class="full">



<tr>

<td style="direction:ltr;text-align:left;padding-top:30px; padding-right:20px; padding-bottom:0px; padding-left:20px;"

class="pt20 ">

<h4

class=""

style="Margin:0;

padding:0;mso-line-height-rule:exactly;

font-family:'Uber Move','HelveticaNeue',

Helvetica,Arial,sans-serif;font-size: 28px;

line-height: 34px;

font-weight: 500;

color:#000000;">

訂餐抽 LINE Points



</td>

</tr>





<tr>

<td height="22"

style="padding-top:10px; padding-right:20px; padding-bottom:30px;padding-left:20px;mso-line-height-rule:exactly;line-height:22px;font-family:'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif;font-size:16px;color:#000000;font-weight:normal;text-decoration:none;"

align="left"

class="">

<div>每週二 / 三 / 四下單用 LINE Pay 單筆訂單滿 $250 累計 5 次，即可參加幸運轉轉樂 1 次，最高可獲得 LINE POINTS <strong>200 點</strong>回饋！</div>



</td>

</tr>







</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</table>

</td>

</tr>



<tr>

<td height="20"

style="font-size:20px;line-height:20px;mso-line-height-rule:exactly;opacity:0;">

&nbsp;&nbsp;

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>





</table>

</td>

</tr>

</table>

</td>

</tr>







<tr>

<td height="15"

style="font-size:15px;line-height:15px;mso-line-height-rule:exactly;opacity:0;#ffffff;">

&nbsp;

</td>

</tr>



</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</table>

</td>

</tr>

</table>

























































































































<table border="0" cellpadding="0" cellspacing="0"

style="border-collapse:collapse;width:100%;direction:ltr;" role="presentation"

bgcolor="#ffffff" data-blockuuid="74d04eee-5b77-4127-9dd8-22a960dc1114">

<tr>

<td class="outsidegutter" align="left"

style="direction:ltr;text-align:left; padding-left: 14px; padding-right: 14px;">

<table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%;"

role="presentation">

<tr>

<td style="direction:ltr;text-align:left;">

<!--[if (gte mso 9)|(IE)]>

<table align="center" cellpadding="0" cellspacing="0" border="0"

role="presentation" style="width:560px;">

<tr>

<td>

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t10of12" align="center"

style="Margin: 0 auto; border-collapse: collapse; max-width: 560px; width: 100%;"

role="presentation">

<tr>

<td style="direction:ltr;text-align:left;">

<table border="0" cellpadding="0" cellspacing="0" width="100%"

align="left"

style="border-collapse: collapse; table-layout: fixed; width: 100%;"

role="presentation">



<tr>

<td height="15"

style="font-size:15px;line-height:15px;mso-line-height-rule:exactly;opacity:0;#ffffff;">

&nbsp;

</td>

</tr>



<tr>





</tr>





<tr>

<td style="direction:ltr;text-align:left;">

<table border="0" cellpadding="0" cellspacing="0" width="100%"

align="left"

style="border-collapse: collapse; table-layout: fixed; width: 100%;"

role="presentation">





































































































































































































































































<!--[if !mso 9]><!-->

<head>

<style type="text/css">

@media screen and (min-width:671px) {

.outlook-mac-fix-left .floatleft {

float: left !important

}

.outlook-mac-fix-right .floatright {

float: right !important

}

}

@media screen and (max-width:430px) {

.heightauto {

height: auto !important

}

.pt20 {

padding-top: 20px !important;

}

.pr20 {

padding-right: 20px !important;

}

.pl20 {

padding-left: 20px !important;

}

.floatleft {

float: left !important;

}

.floatright {

float: right !important;

}

}

</style>

</head>

<!--<![endif]-->









<tr data-blockuuid="569b6804-41ce-4801-98dd-81f82c78e1b2">

<td style="font-size:1px;line-height:1px;vertical-align:top;padding-left:12px;padding-right:12px;"

valign="top" align="left">

<!--[if (gte mso 9)|(IE)]>

<table align="left" cellpadding="0" cellspacing="0" border="0" role="presentation"

style="width:536px;">

<tr>

<td width="536">

<![endif]-->

<table width="536" border="0" cellspacing="0" cellpadding="0" align="left"

role="presentation"

style="width:100%;max-width:536px;direction:ltr;text-align:left;">



<tr>

<td style="font-size:1px;line-height:1px;border-radius:10px;" bgcolor="#d3efda"

align="left">

<table style="width:100%;border-radius:10px;" cellpadding="0" cellspacing="0" border="0"

align="left" role="presentation">

<tr>

<td style="font-size:1px;line-height:1px;vertical-align:middle;border-radius:10px;"

valign="middle" align="left">

<!--[if (gte mso 9)|(IE)]>

<table align="left" cellpadding="0" cellspacing="0"

border="0" role="presentation" style="width:536px;">

<tr>

<td width="536">

<![endif]-->

<table border="0" cellspacing="0" cellpadding="0"

align="left"

style="width:100%;max-width:536px;vertical-align:middle;"

role="presentation">

<tr>

<td style="vertical-align:middle;" valign="middle">

<!--[if (gte mso 9)|(IE)]>

<table align="left"

cellpadding="0" cellspacing="0" border="0"

role="presentation"

style="width:238px;direction:ltr;vertical-align:middle;">

<tr>

<td width="238"

style="font-size:1px;line-height:1px;vertical-align:middle;"

align="left">

<![endif]-->

<table border="0" cellspacing="0"

cellpadding="0"

align="left"

role="presentation"

style="width:100%;max-width:238px;direction:ltr;vertical-align:middle;float:left;"

class="full floatleft outlook-mac-fix-left">

<tr>

<td style="font-size:1px;line-height:1px;vertical-align:middle;"

valign="middle"

align="left"

height="278"

class="heightauto">

<table

width="218"

border="0"

cellspacing="0"

cellpadding="0"

align="left"

role="presentation"

style="direction:ltr;text-align:left;width:100%;max-width:430px;vertical-align:middle;">

<tr>

<td style="direction:ltr;text-align:left;padding-left:20px;padding-top:30px;padding-bottom:30px;vertical-align:middle;"

align="left"

valign="middle"

class="hide414">



<img src="https://d1g1f25tn8m2e6.cloudfront.net/be61139d-3bb1-421d-99f0-11ea03d082e2.png"

alt="1"

title="1"

width="218"

height="218"

border="0"

style="vertical-align:middle;display:inline-block!important;font-family:'Uber Move','HelveticaNeue',Helvetica,Arial,sans-serif;font-size:14px;line-height:17px;color:#000000;font-weight:500;text-decoration:none;width:100%;max-width:238px;height:218px;" />



</td>

<!--[if !mso 9]><!-->

<td style="direction:ltr;text-align:left;padding-left:20px;padding-right:20px;padding-top:30px;;vertical-align:middle;display:none;overflow:hidden;max-height:0;mso-hide:all;"

align="left"

valign="middle"

class="show414">



<img src="https://d1g1f25tn8m2e6.cloudfront.net/be61139d-3bb1-421d-99f0-11ea03d082e2.png"

alt="1"

title="1"

width="218"

height="218"

border="0"

style="vertical-align:middle;display:inline-block!important;font-family:'Uber Move','HelveticaNeue',Helvetica,Arial,sans-serif;font-size:14px;line-height:17px;color:#000000;font-weight:500;text-decoration:none;width:100%;max-width:218px;height:auto;" />



</td>

<!--<![endif]-->

</tr>

</table>

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

<td width="298"

style="font-size:1px;line-height:1px;"

align="center">

<![endif]-->

<table border="0" cellspacing="0"

cellpadding="0" align="center"

style="width:100%;max-width:298px;float:right;"

role="presentation"

class="full floatright outlook-mac-fix-right">

<tr>

<td style="font-size:1px;line-height:1px;vertical-align:middle;"

valign="middle"

align="left"

height="278"

class="heightauto">

<!--[if (gte mso 9)|(IE)]>

<table

align="left"

cellpadding="0"

cellspacing="0"

border="0"

role="presentation"

style="width:298px;">

<tr>

<td

width="298">

<![endif]-->

<table

border="0"

cellspacing="0"

cellpadding="0"

align="center"

style="width:100%;max-width:298px;"

role="presentation"

class="full">



<tr>

<td style="direction:ltr;text-align:left;padding-top:30px; padding-right:20px; padding-bottom:0px; padding-left:20px;"

class="pt20 ">

<h4

class=""

style="Margin:0;

padding:0;mso-line-height-rule:exactly;

font-family:'Uber Move','HelveticaNeue',

Helvetica,Arial,sans-serif;font-size: 28px;

line-height: 34px;

font-weight: 500;

color:#000000;">

新用戶滿額折



</td>

</tr>





<tr>

<td height="22"

style="padding-top:10px; padding-right:20px; padding-bottom:30px;padding-left:20px;mso-line-height-rule:exactly;line-height:22px;font-family:'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif;font-size:16px;color:#000000;font-weight:normal;text-decoration:none;"

align="left"

class="">

<div>Uber Eats 新用戶輸入<strong>【賴配歡迎你】</strong>，訂單滿 $299 可享 2 次 <strong>$150</strong> 折抵優惠！(即日起至 2024/6/30)</div>



</td>

</tr>







</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</table>

</td>

</tr>



<tr>

<td height="20"

style="font-size:20px;line-height:20px;mso-line-height-rule:exactly;opacity:0;">

&nbsp;&nbsp;

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>





</table>

</td>

</tr>

</table>

</td>

</tr>









<tr>

<td height="30"

style="font-size:30px;line-height:30px;mso-line-height-rule:exactly;opacity:0;#ffffff;">

&nbsp;

</td>

</tr>



</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</table>

</td>

</tr>

</table>

























































































































































































 

 



















































































   









































    























  

  



  

    

  





  

  



  

  

  



  

    

  













<!--  B_IMG_COPY 1.1  cf 6/9/20 -->

<table width="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%;" data-blockuuid="6f3b69d1-a5d5-4932-81ad-5273fe7d6741">

<tbody>

<tr>

<td class="outsidegutter" align="left" style="direction:ltr;text-align:left; padding-left: 14px;padding-right: 14px;padding-top: 30px;padding-bottom: 30px; background-color:#f3f3f3;">

<table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse; width: 100%;">

<tbody><tr>

<td style="direction:ltr;text-align:left;">

<!--[if (gte mso 9)|(IE)]>

<table width="560" align="center" cellpadding="0" cellspacing="0" border="0">

<tr>

<td>

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t10of12" align="center" style="Margin: 0 auto; border-collapse: collapse; max-width: 560px; width: 100%;">

<tbody><tr>

<td style="  direction:rtl; text-align:left;padding-left: 0; padding-right: 0; font-size:0; padding-top:10px;">

<!--[if (gte mso 9)|(IE)]>

<table width="560" align="left" cellpadding="0" cellspacing="0" border="0">

<tr>

<td width="280" valign="middle">

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t5of12"  style="border-collapse: collapse; max-width: 280px; width: 100%; display: inline-block; vertical-align: middle;">

<tbody><tr>

<td style="direction:ltr;text-align:left;padding-left: 12px; padding-right: 12px;">

<table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="border-collapse: collapse; table-layout: fixed; width: 100%;">

<tbody>

<tr>

<td>









<tr>

<td style="direction:ltr; text-align:left;">

<table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="border-collapse: collapse; table-layout: fixed; width: 100%;">

<tbody>

<tr>



<td style="direction:ltr; text-align:left; Margin: 0; font-family: 'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif; font-size: 20px; line-height: 26px; padding:7px 0 10px 0; font-weight: 700; color: #000000;" class="" valign="top">✦ <strong>LINE Pay 一鍵下單攻略</strong>



</td>



</tr>

</tbody>

</table>

</td>

</tr>







<tr>

<td class="p2" style="direction:ltr; text-align:left; font-family: 'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 22px; color: #000000; padding:0 0 15px 0;"><div>步驟一：<br />

<strong>更新 Uber Eats App 至最新版本</strong><br />

<br />

步驟二：<br />

➀ 下單時付款方式選擇 👉🏻 <strong>LINE Pay</strong><br />

➁ 畫面點擊 <strong>[重新連線至 LINE Pay]</strong><br />

➂  前往 LINE Pay 頁面，<strong>完成 LINE Pay 預設扣款信用卡設定</strong><br />

<br />

😎 完成啦！未來下單無需再跳轉至 LINE Pay，就是這麼簡單！<br />

</div>



</td>

</tr>







</td>

</tr>

</tbody></table>

</td>

</tr>

</tbody></table>

<!--[if (gte mso 9)|(IE)]>

</td>

<td width="280" valign="middle">

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t5of12" style="border-collapse: collapse; max-width: 280px; width: 100%;display: inline-block; vertical-align: middle;">

<tbody><tr>

<td style="direction:ltr;text-align:left;padding-left: 12px; padding-right: 12px;">

<table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="border-collapse: collapse; table-layout: fixed; width: 100%;">

<tbody><tr>

<td style="padding:10px 0 20px 0;">



<img src="https://d1g1f25tn8m2e6.cloudfront.net/64121d19-5a58-4ce6-bc33-69fd625e5e9a.gif" width="256" height="" style="display: block; width:100%; max-width: 256px; height:auto; outline: none; text-decoration: none;" border="0" alt="LINE Pay">



</td>

</tr>

</tbody></table>

</td>

</tr>

</tbody></table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</tbody></table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</tbody></table>

</td>

</tr>

</tbody></table>

<!--  close B_IMG_COPY B3  -->











</td>

</tr>

</tbody>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</tbody>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</tbody>

</table>

</td>

</tr>

</tbody>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</tbody>

</table>

<!-- END LIST-->

</td>

</tr>

<!-- END BODY-->

</tbody>

</table>



<!-- ces update pm logo swap --> 



















































































































  

  

  



  

  

  

  



   

  

  



  

  

  



  

  

  



  

    

    

    

    

    



  





  



  

  

  

  



   

  

  



  

  

  



  

  

  



  

    

    

    

    

    

  





  



  

  

  

  



   

  

  



  

  

  



  

  

  



  

    

    

    

    

    

  





  



  

  

  

  



   

  

  



  

  

  



  

  

  



  

    

    

    

    

    

  









  

  

  

  



  

  

    

  

  



  

    

    

  



  

  

  



  











































<!-- footer update 07/13/2022 MT -->

<table width="100%" border="0" cellpadding="0" cellspacing="0" style="background-color: #000000; width: 100%;" data-blockuuid="beecfab4-37bc-4788-b50f-ca473abf4bf3">

<tr>

<td class="outsidegutter" align="left" style="direction:ltr;text-align:left; padding-top: 30px">

<table border="0" cellpadding="0" cellspacing="0" style="width: 100%;" class="">









<!-- Top half -->





<!-- Legal Disclaimer -->



  

  



  

  



  

  



  

  

  

  

  

  



<!-- Legal Disclaimer -->



<tr>

<td style="direction:ltr;text-align:left;padding: 0px 14px 30px 14px;">

<!--[if (gte mso 9)|(IE)]>

<table width="560" align="center" cellpadding="0" cellspacing="0" border="0">

<tr>

<td>

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t10of12" align="center" style="Margin: 0 auto; max-width: 560px; width: 100%;">

<tr>

<td>

<table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="direction: rtl; table-layout: fixed; width: 100%;">

<tr>

<td class="ignoreTd" style="font-size:0; text-align: left;">

<table border="0" cellpadding="0" cellspacing="0" class="t6of12" style="direction: ltr; display: inline-block; max-width: 560px; vertical-align: top; width: 100%;">

<tr>

<td>

<table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="table-layout: fixed; width: 100%;">

<tr>

<td>

<!--[if (gte mso 9)|(IE)]>

<table width="468" align="left" cellpadding="0" cellspacing="0" border="0">

<tr>

<td width="168">

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t3of12" align="left" style="max-width: 168px; width: 100%;">

<tr>

<td style="direction:ltr;text-align:left;padding: 0 12px;">

<table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="table-layout: fixed; width: 100%;">







  































<tr>

<td class="white" style="color:#ffffff; font-family: 'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif; font-size: 12px; line-height: 18px; padding: 3px 0px; direction: ltr; text-align: left;">

<a href="http://email.uber.com/ss/c/u001.Z92I9v7tcN2DT5AZgXa6lrdDSsKtGqspS3jnrmUWYPe-WC9j5FDOiowBqLnkwSil/47c/bwGpxaGZT4GyP2v76A_9_Q/h4/h001.sdAS7zAMM-40kjSBtj1QLfA7hJeadlrXSx6OyeJnaO4" style="color: #ffffff; text-decoration: none;">客服中心</a>

</td>

</tr>



  































<tr>

<td class="white" style="color:#ffffff; font-family: 'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif; font-size: 12px; line-height: 18px; padding: 3px 0px; direction: ltr; text-align: left;">

<a href="http://email.uber.com/ss/c/u001.3rz4IfclD0-2ph6Eff9d69FeoNWZ7HJlckoipfD4Y0E51tkiUwjlOABgER80fiIW/47c/bwGpxaGZT4GyP2v76A_9_Q/h5/h001.Jf5zOZg6HvW22llA1qiMyFhBmyHbWIQCz2c0bsjKdjM" style="color: #ffffff; text-decoration: none;">條款</a>

</td>

</tr>





  

  





























  

    

    

  





<tr>

<td class="white" style="color:#ffffff; font-family: 'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif; font-size: 12px; line-height: 18px; padding: 3px 0px; direction: ltr; text-align: left;">

<a href="http://email.uber.com/ss/c/u001.3rz4IfclD0-2ph6Eff9d62l6WT6qKAZ6xAyGls9kuW3g7Hot5Mw9UjqwSrge8UXCVT-Eot4IPruwNq9cqkQOv1SYPmiyBZXDA1RG6ZIdRUJ2aUXftu3CaNC5PV4BGgnurewaKKN_WKgf8mKcmKHqgyyP3oaOJ2TUXzdT_yqyxeGmBBfGdMMadOFrlwwtY8dcBw0wM4jpkrgRJWAZowTR73ebrhqNdlfOhF2Q_XGW-hKURTne8txLKy_BbmRAVBHYcfffgnHl02nh-2upk5R7cxkhpmOUE-xBSGhWvxJC-3p2xU5eZcUshGUJ38JEiB9PdobJYC7atPULTmyNXekaFadvewUfzeEqpGa-bxdQX9nih_J31ycvgam892ODM4As6g_d9Ld7ErhyR_WF2pCJsxY1JXwjQW1V5PQkpC5QS1X735G_cjG5unUnPAGTv0rzkkCfl5ijaild_q3Tnax5DPaMgEuv0iktNpeuUtsZxENmClgtxyM0XjDh0MNPcVnalESMUeeHhxskRfERtoiLbqhraFxu5Q1QdYJIVR9toXgAtZf2SuxK122MpWJeYIj77_vl4laa_fJ8dmCP9oDXpkL2jUuPp2fRgVlOID_rBE8y8xMdHjNjiDujr0gafZrFWIvOhWRSPEKxo2brHfKTMY0gd2ZujOB_AAfNjEXnVo56HOa0A-T9N4kiNzEJ0WaNN2V650rOBU9IVVSX4pYdi87onp5GjBzTHE2YtcajZlejB3FmRj-jdP5JWKDAToD1T8oQEGSklQ8LolQ_8POsJO68urPi6hdTSuGfeqtahwGHL9uQ8rNhTj-TaXfiWIww_RzpWjyXa5KD0H55jZbTuNzKBiteoyz9lwzKOp8qM6zVkLq615fC1VahoUONIGXN6097Ds0pPPv5rHdISZr_wSSTj0KG8sSb0h3eT9-nowfUXA5fpeCHaFbV1vFqBA8ehAivQvz2KalPxbo73jomfnXnfCGX6PtdrQL83zBqww6wMMXymbjNvut2Wbmdu_0Xlp-RLLEoesPo8EsHtP1D8EFoBsooCnNzyMy-SUBQVe0GYVbhYEL7mhsX87nCbR22PoPeGaCQdVFDudYQTamqYhIpci6rLTHSVsm8tZCUgUBfiU9-ujhuHO9qN4nwAkaZtIhxKgls3h0imKIkgmOXIGe2dZ9eEAKzONCCqnfm1lUdDAKNc8I6SJ1xF3NsvH7o/47c/bwGpxaGZT4GyP2v76A_9_Q/h6/h001.QQ3kHiD2TUmkNAxWY3rVUiFFxRIw13MBj6bDqF-ZDHQ" style="color: #ffffff; text-decoration: none;">取消訂閱</a>

</td>

</tr>



  



  



























</table>

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>



<td width="300" valign="top" style="vertical-align: top;">

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t3of12" align="left" style="max-width: 300px; width: 100%;">

<tr>

<td style="direction:ltr;text-align:left;padding: 0 12px;">

<table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="table-layout: fixed; width: 100%;">







  































<tr>

<td class="white" style="color:#ffffff; font-family: 'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif; font-size: 12px; line-height: 18px; padding: 3px 0px; direction: ltr; text-align: left;">

<a href="http://email.uber.com/ss/c/u001.JfX2-y9ZMfLbJ6S_zqCLfayu1d2hl_2Q2KYfMC3I5ZVUoVmAAYiLbTL2GZlbo1Yh/47c/bwGpxaGZT4GyP2v76A_9_Q/h7/h001._aa-iNK10YYiPB1ioPgNbKGEFc0k23KucTntV_lCWpI" style="color: #ffffff; text-decoration: none;"> 隱私權</a>

</td>

</tr>



  

   































<tr>

<td class="white" style="color:#ffffff; font-family: 'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif; font-size: 12px; line-height: 18px; padding: 3px 0px; direction: ltr; text-align: left;">

<a href="http://email.uber.com/ss/c/u001.4ExuDpoZDQKZIscLSzLJVs_uGuYqLGUASHT-0vjc6-KcZvNr-xQlSIW3JPLF9zDQ/47c/bwGpxaGZT4GyP2v76A_9_Q/h8/h001.TvoSfgXTz_PjKcbcLmZ6L_UHBj1vigVhnGnT5NasINI" style="color: #ffffff; text-decoration: none;">電子郵件偏好設定</a>

</td>

</tr>

 























</table>

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>





</tr>

</table>

<![endif]-->

</td>

</tr>

</table>

</td>

</tr>

</table>



</td>

</tr>

</table>

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

<!-- END top half -->





<!-- bottom half -->

<tr>

<td style="direction:ltr;text-align:left; padding: 0px 14px 30px 14px;">

<!--[if (gte mso 9)|(IE)]>

<table width="560" align="center" cellpadding="0" cellspacing="0" border="0">

<tr>

<td width="560">

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t10of12" align="center" style="Margin: 0 auto; max-width: 560px; width: 100%;">

<tr>

<td>

<table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="direction: rtl; table-layout: fixed; width: 100%;">

<tr>

<td style="font-size:0; text-align: left">

<!--[if (gte mso 9)|(IE)]>

<table width="560" align="left" cellpadding="0" cellspacing="0" border="0">

<tr>

<td width="224">

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t4of12" style="direction: ltr; display: inline-block; max-width: 224px; vertical-align: top; width: 100%;">

<tr>

<td style="direction:ltr;text-align:left;padding: 0 12px;">

<table border="0" cellpadding="0" cellspacing="0"  align="left" style="table-layout: fixed;">

<tr>

<td style="padding-bottom: 12px; direction:ltr;text-align:left;">



<!-- social table -->

<table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="table-layout: fixed; width: 130px;">

<tr>

<td width="43" align="center" style="direction: ltr; text-align: left;">

<a href="http://email.uber.com/ss/c/u001.3rz4IfclD0-2ph6Eff9d66wdDEvXjrbEDt9pz5vdBGRoNk88CTLSg6AO2xKvXH5G/47c/bwGpxaGZT4GyP2v76A_9_Q/h9/h001.BVpUOQhe5ivG73SLEQUFkpPPrLNeYNLh7P7QChoptaU"> <img src="https://d3smpkehiq8afm.cloudfront.net/assets/icons/social_darkmode/social_icons_071522/social-icon-facebook-black.png" width="32" height="32" border="0" style="display: block; height: auto; max-height: 32px; max-width: 32px; width: 100%;">

</a>

</td>

<td width="43" align="center" style="direction: ltr; text-align: left;">

<a href="http://email.uber.com/ss/c/u001.mspHjJOk8JIj3l-SrEEc6RgU3mYfceK5MxuC1fXMaqw/47c/bwGpxaGZT4GyP2v76A_9_Q/h10/h001.2Y06xor334GmUAkgjIn2vfjyKeyYcgMrVdL1yzRbpho"> <img src="https://d3smpkehiq8afm.cloudfront.net/assets/icons/social_darkmode/social_icons_071522/social-icon-twitter-black.png" width="32" height="32" border="0" style="display: block; height: auto; max-height: 32px; max-width: 32px; width: 100%;">

</a>

</td>

<td width="43" align="center" style="direction: ltr; text-align: left;">

<a href="http://email.uber.com/ss/c/u001.3rz4IfclD0-2ph6Eff9d60ryYi1OKRcOapk6BJhmUWwiICBglVglqiC8NcDPmUZ7/47c/bwGpxaGZT4GyP2v76A_9_Q/h11/h001.xEgJE85o_yYUWMS6jjmw6C44zXoJpVki2VuysSkHEaU"> <img src="https://d3smpkehiq8afm.cloudfront.net/assets/icons/social_darkmode/social_icons_071522/social-icon-instagram-black.png" width="32" height="32" border="0" style="display: block; height: auto; max-height: 32px; max-width: 32px; width: 100%;">

</a>

</td>

</tr>

</table>

<!-- END social table -->



</td>

</tr>

</table>

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

<td width="336">

<![endif]-->

<table border="0" cellpadding="0" cellspacing="0" class="t6of12" style="direction: ltr; display: inline-block; max-width: 336px; vertical-align: top; width: 100%;">

<tr>

<td style="direction:ltr;text-align:left;padding: 0 12px;">

<table border="0" cellpadding="0" cellspacing="0" width="100%" align="left" style="table-layout: fixed; width: 100%;">

<tr>

<td style="direction:ltr;text-align:left;color: #e5e5e5; font-family: 'Uber Move Text', 'HelveticaNeue', Helvetica, Arial, sans-serif; font-size: 10px; line-height: 18px;">















Uber Portier TW <br> 3F., No. 27, Wuquan 5th Rd., Wugu Dist.,<br> New Taipei City 248, Taiwan (R.O.C.)  



<br>



<a href="http://email.uber.com/ss/c/u001.D99t-Ta36h6Fmg_QWyqx8x9EYQwcF7wsrJii1Zqbvvs/47c/bwGpxaGZT4GyP2v76A_9_Q/h12/h001.R1cMJkiP31XYz8PVsxgdQKq7zHa-gtf_iCrNttXuYxU" style="text-decoration: none; color: #e5e5e5">Uber.com</a>



</td>

</tr>

</table>

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</table>

</td>

</tr>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

<!-- END bottom half -->





</table>

</td>

</tr>

</table>

<!-- close footer update - MT -->











</td>

</tr>

</tbody>

</table>

<!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->

</td>

</tr>

</tbody>

</table>



<img src="http://email.uber.com/ss/o/u001.NY4fipz4LeOAyyRQlF-n1Q/47c/bwGpxaGZT4GyP2v76A_9_Q/ho.gif" alt="" width="1" height="1" border="0" style="height:1px !important;width:1px !important;border-width:0 !important;margin-top:0 !important;margin-bottom:0 !important;margin-right:0 !important;margin-left:0 !important;padding-top:0 !important;padding-bottom:0 !important;padding-right:0 !important;padding-left:0 !important;"/></body></html>


"""

# Extract text from the example HTML
extracted_text = extract_text_from_html(html_content)

# Write the extracted text to a Markdown file
output_filename = 'output.md'
write_to_markdown_file(extracted_text, output_filename)

print(f"Extracted text has been written to {output_filename}")
