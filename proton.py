import tempfile
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
#from supabase import create_client, Client


url_ = "https://jdnmanfimzvbilacjgcj.supabase.co"
key = "sb_secret_eVYWCtpPzmFsbJryaEug0A_EYBBcCII"

#supabase: Client = create_client(url_, key)


"""
python proton_send.py
"""

profile_dir = tempfile.mkdtemp()
chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")
chromedriver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")

url = "https://account.proton.me/mail"
options = Options()
options.binary_location = chrome_bin
options.add_argument("--headless")
options.add_argument(f"--user-data-dir={profile_dir}")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
#driver = webdriver.Chrome(options=options)
#driver.maximize_window()
driver.get(url)
actions = ActionChains(driver)

def insert_script(el_selector, value):
    src = f"""
        function setNativeValue(element, value) {{
          const lastValue = element.value;
          element.value = value;

          const event = new Event("input", {{ bubbles: true }});

          const tracker = element._valueTracker;
          if (tracker) tracker.setValue(lastValue);

          element.dispatchEvent(event);
        }};
        let usna = "{value}"
        let selector = document.querySelector('[{el_selector}]')
        setNativeValue(selector, usna)
        """
    return src
thus = True
def into_true(to):
    src = f"""
        function setNativeValue(element, value) {{
          const lastValue = element.value;
          element.value = value;

          const event = new Event("input", {{ bubbles: true }});

          const tracker = element._valueTracker;
          if (tracker) tracker.setValue(lastValue);

          element.dispatchEvent(event);
        }};
        let to_ = "{to}"
        const toInput =
        document.querySelector('[data-testid="composer:to"]') ||
        document.querySelector('input[placeholder*="To"]') ||
        document.querySelector('input[type="email"]');

        // If found, set the recipient properly
        if (toInput) {{
          setNativeValue(toInput, to_);

          // ProtonMail requires ENTER to convert the input into an email chip
          toInput.dispatchEvent(new KeyboardEvent("keydown", {{ key: "Enter", bubbles: true }}));
          toInput.dispatchEvent(new KeyboardEvent("keyup", {{ key: "Enter", bubbles: true }}));
        }}
    """
    return src
def into_true_1():
    src = f"""
      let res = false
      const toInput =
      document.querySelector('[data-testid="composer:to"]') ||
      document.querySelector('input[placeholder*="To"]') ||
      document.querySelector('input[type="email"]');

    // If found, set the recipient properly
    if (toInput) {{
        res = true
    }}
    return res
    """
    return src
def insert_letter(em, of_id):
    src = f"""
        document.querySelector('[title="Éditeur de messages"],[title="Email composer"]').contentDocument.querySelector('[id="rooster-editor"]').innerHTML = `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
			<html xmlns="http://www.w3.org/1999/xhtml">
			
			<head>
			  <title></title>
			
			  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
			  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
			  <meta name="format-detection" content="telephone=no"/>
			  <meta name="format-detection" content="date=no"/>
			  <meta name="format-detection" content="address=no"/>
			  <meta name="format-detection" content="email=no"/>
			  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
			
			  <style type="text/css">
				body	{{Margin:0 auto; padding:0;}}
				img		{{max-width:100%;}}
				table	{{border-spacing:0!important; border:none; cellpadding:0px; }}
				td		{{cellpadding:0px; border-spacing:0px;}}
				tr		{{cellpadding:0px; border-spacing:0px;}}
			/* GK: Client-specific Styles */
				#outlook a{{padding:0;}} /* GK: Force Outlook to provide a "view in browser" message */
				.ReadMsgBody{{width:100%;}} .ExternalClass{{width:100%;}} /* GK: Force Hotmail to display emails at full width */
				.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {{line-height: 100%;}} /* GK: Force Hotmail to display normal line spacing */
				body, table, td, a{{-webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;}} /* GK: Prevent WebKit and Windows mobile changing default text sizes */
				table, td{{mso-table-lspace:0pt; mso-table-rspace:0pt;}} /* GK: Remove spacing between tables in Outlook 2007 and up */
				img{{-ms-interpolation-mode:bicubic;}} /* GK: Allow smoother rendering of resized image in Internet Explorer */			
			  </style>
			</head>
			
			
			<body bgcolor="#f2f2f2">
			
			<!-- GK: container  -->
			  <table width="100%" border="0" cellpadding="0" cellspacing="0" id="wrappertable" style="table-layout: fixed;">
				<tr>
				  <td align="center" valign="top" >
					<table cellpadding="0" cellspacing="0" border="0">
					  <tr>
						<td width="600" align="center" valign="top" style="background-color: #ffffff; box-shadow: 1px 1px 10px 0px rgba(25, 25, 25, 0.15);">
							<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #151515;">
									  <tr>
										<td align="center" valign="middle" style="font-family:Arial, Helvetica, sans-serif; font-size:16px; font-weight:normal; line-height:22px; letter-spacing:0px; color:#ffffff;  min-height:20px; mso-line-height-rule: exactly; padding: 20px 25px;"><strong>Wir gratulieren Ihnen recht herzlich!</strong>
			
										</td>
									  </tr>
									</table>
			<!-- GK: image-->
						  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; padding:0px 0px 10px 0px;">
							<tr>
							  <td valign="middle" style=" line-height:1px;">
							  </td>
							</tr>
							<tr>
							  <td align="center" valign="top" style="padding: 0 0px;">
								<table cellpadding="0" cellspacing="0" border="0">
								  <tr>
									<td width="600" align="center" valign="middle" >
									  <a href="https://vptrmftnkfewhscirhqe.supabase.co/functions/v1/trk1_clk?em_ofid={em}|{of_id}" style="outline:0;" target="_blank">
										<img src="https://vptrmftnkfewhscirhqe.supabase.co/functions/v1/img_op_gml?em_ofid={em}|{of_id}" style="width: 100%; max-width: 100%; margin: 0px 0;" border="0" alt=""/>
									  </a>
							
									</td>
								  </tr>
								</table>
							  </td>
							</tr>
						  </table>
			<!-- GK: end image -->
					 <!-- GK: CTA (Button) -->
								  <table width="60%" cellpadding="0" cellspacing="0" border="0">
									<tr>
									  <td align="center" valign="top" style="padding: 0 20px;">
										<table cellpadding="0" cellspacing="0" border="0">
												 <tr>
											<td width="350" align="center" valign="top">
											  <table width="100%" cellpadding="0" cellspacing="0" border="0">
												<tr>
												  <td width="350" height="40" align="center" valign="middle" style="background-color:#ff9900; padding: 6px 12px; ">
													<a style="display: block; text-decoration: none; font-family: 'Arial', verdana, sans-serif; font-size: 18px; mso-line-height-rule: exactly; line-height: 32px;font-weight: bold; color: #ffffff;" href="https://vptrmftnkfewhscirhqe.supabase.co/functions/v1/trk1_clk?em_ofid={em}|{of_id}" target="_blank"> 
														 Jetzt gewinnen!
													</a>
												  </td>
												</tr>
											  </table>
											</td>
										  </tr>
										</table>
									  </td>
									</tr>
								  </table>
			<!-- GK: end CTA (Button) -->
			<!-- GK: spacer -->
						  <table width="100%" cellpadding="0" cellspacing="0" border="0">
							<tr>
							  <td style="line-height: 0px;">
							  </td>
							</tr>
						  </table>
			<!-- GK: end spacer -->
			
			<!-- GK: text content -->
						  <table width="100%" cellpadding="0" cellspacing="0" border="0" >
							<tr>
							  <td align="center" valign="middle" style="font-family:Arial, Helvetica, sans-serif; font-size:16px; font-weight:normal; line-height:22px; letter-spacing:0px; color:#414141; padding-left:10px; padding-right:10px; min-height:20px; mso-line-height-rule: exactly; padding: 0px 25px;">
								  <br />
								  Nach einem speziellen Verfahren wurde Ihre E-Mail-Adresse ausgewählt:<br />
			
			( {em} )<br />
			<br />
			Sie haben es GESCHAFFT – Sie sind dabei!</strong><br />
			<br />
			
							  Wir freuen uns Ihnen mitzuteilen, dass Sie einer von 4 Teilnehmern in der Endauslosung sind. Sie haben jetzt die einmalige Chance, ein gratis &nbsp; <strong><br />
			 1.000€ AMAZON-Gutschein + iPhone 15 Pro Max</strong> zu gewinnen! <br />
			<br />
			Die anderen Teilnehmer in der Endauslosung sind: <br />
			1. Manuela Ö***<br />
			
			2. Dominik L***<br />
			
			3. Hermina T***<br />
			<br />
			
			 
			Jetzt schnell und einfach eintragen und qualifizieren Sie sich noch heute!<br />
			<br />
			
			 
			Wir wünschen viel Spaß und Erfolg!<br />
			
			Ihr Noah Müller vom Gutschein-Team
			 <br />
			<!-- GK: end text content -->
			
			<!-- GK: spacer -->
								  <table width="100%" cellpadding="0" cellspacing="0" border="0">
									<tr>
									  <td style="padding-top: 10px; line-height: 0px;">
									  </td>
									</tr>
								  </table>
			<!-- GK: end spacer -->
			
			<!-- GK: CTA (Button) -->
								  <table width="70%" cellpadding="0" cellspacing="0" border="0">
									<tr>
									  <td align="center" valign="top" style="padding: 0 20px;">
										<table cellpadding="0" cellspacing="0" border="0">
										  <tr>
											<td style="padding-top: 5px; line-height: 0px;">
											</td>
										  </tr>
										  <tr>
											<td width="350" align="center" valign="top">
											  <table width="100%" cellpadding="0" cellspacing="0" border="0">
												<tr>
												  <td width="350" height="40" align="center" valign="middle" style="background-color:#ff9900; padding: 6px 12px; ">
													<a style="display: block; text-decoration: none; font-family: 'Arial', verdana, sans-serif; font-size: 18px; mso-line-height-rule: exactly; line-height: 32px;font-weight: bold; color: #ffffff;" href="https://vptrmftnkfewhscirhqe.supabase.co/functions/v1/trk1_clk?em_ofid={em}|{of_id}" target="_blank"> 
														 Jetzt mitmachen!
													</a>
												  </td>
												</tr>
											  </table>
											</td>
										  </tr>
										</table>
									  </td>
									</tr>
								  </table>
			<!-- GK: end CTA (Button) -->
			
								</td>
							  </tr>
							</table>
			
			<!-- GK: spacer -->
							<table width="100%" cellpadding="0" cellspacing="0" border="0">
							  <tr>
								<td style="padding-top: 40px; line-height: 0px;">
								</td>
							  </tr>
							</table>
			<!-- GK: end spacer -->
			
			<!-- GK: spacer -->
							<table width="100%" cellpadding="0" cellspacing="0" border="0" style=" background-color: #151515;">
							  <tr>
								<td style="padding-top: 60px; line-height: 0px;">
								</td>
							  </tr>
							</table>
			<!-- GK: end spacer -->
			
						</td>
					</tr>
				  </table></td>
			  </tr>
			</table>
			<!-- end container -->
			
			<img src="https://we-do-xter.com/i.ashx?E=XYd4Y%2fo%2bvgQgY1ISRTAu583Z2lyxeAsH&s1=SUB_ID" width="1" height="1" border="0" /></body>
			</html>`
    """
    return src
ems = [
    "zhoridlono@web.de",
    "DonasKarine13@gmx.fr",
    "adamoyler2705cc@web.de",
    "hermanhunter1174cc@web.de",
    "arbi.naji@gmail.com",
    "joehalivy@gmail.com",
    "adamhardison284@gmail.com",
]
for x in ems:
    while thus:
        user_names = driver.execute_script("return document.querySelectorAll('[id=\"username\"]')")
        if len(user_names) > 0:
            driver.execute_script(insert_script('id="username"', 'BennettPatel880@proton.me'))
            time.sleep(3)
            driver.execute_script(insert_script('id="password"', 'ArbiNaji1987$'))
            time.sleep(3)
            driver.execute_script("document.querySelector('[class=\"button w-full button-large button-solid-norm mt-6\"]').click()")
            th_new_mail = True
            while th_new_mail:
                new_mails = driver.execute_script("return document.querySelectorAll('[class=\"button button-large button-solid-norm w-full hidden md:inline\"]')")
                if len(new_mails) > 0:
                    driver.execute_script("document.querySelector('[class=\"button button-large button-solid-norm w-full hidden md:inline\"]').click()")
                    time.sleep(2)
                    th_new_mail = False
            th_rec = True
            while th_rec:
                rec_res = driver.execute_script(into_true_1())
                if rec_res:
                    driver.execute_script(into_true(x))
                    time.sleep(1)
                    th_rec = False
            th_sbject = True
            while th_sbject:
                subjects = driver.execute_script("return document.querySelectorAll('[data-testid=\"composer:subject\"]')")
                if len(subjects) > 0:
                    driver.execute_script(insert_script('data-testid="composer:subject"', "Nur heute: Sichern Sie sich Ihre Gewinnchance!"))
                    time.sleep(1)
                    th_sbject = False
            th_text_area = True
            while th_text_area:
                text_areas = driver.execute_script("return document.querySelectorAll('[title=\"Éditeur de messages\"],[title=\"Email composer\"]')")
                if len(text_areas) > 0:
                    driver.execute_script(insert_letter(x, "8"))
                    time.sleep(2)
                    driver.execute_script("document.getElementsByClassName('button button-group-item button-medium button-solid-norm composer-send-button')[0].click()")
                    th_text_area = False
                    
            
            time.sleep(5)
            thus = False
