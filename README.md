Name:StrucOGP

version:1.0.0

release date: 11/15/2025

developed by python3.9



System requirements

Operating system and software

Windows 11、10 or Windows 7 Service Pack 1 above, Windows Server 2012 or above.

Hardware

Intel or AMD x86-64 processor, 4.6 GHz processor with 64 GB RAM





Installation guide

StrucOGP can be used without installation.





How to acquire StrucOGP license to activate your StrucOGP software:



1\. You can input 'ipconfig/all' in your command prompt window(CMD) on Windows platform. Under "Ethernet adapter" you may find a string consisting of 12 hexadecimal digits after the "Physical Address", which is your device's media access control address(MAC Address).



2\. After getting your MAC address, you need to copy it next to "MAC" between the "####" chars.



3\. Besides, in order to get closer contact with users. You need to fill all below items between the "####" chars. You can just send this README txt file to sun\_glycolab@126.com after finish it and we will provide StrucOGP license to you as soon as possible.



4\. You will find a LIC file named StrucOGP\_license in our reply. Please put it in the same folder as the main.exe. The wrong path or license file may cause failure when you start program.

 

5\. StrucOGP is available freely for academic research, non-commercial or educational purposes under academic license.



6\. If there are any other errors when you activate or use StrucOGP, Please contact with us via sun\_glycolab@126.com.





\#####################################################################



MAC:



User Name:



Your e-mail address:



University or Organization name:



Country or Region:



Your Leader or Supervisor:



Your leader's e-mail:



\#####################################################################







Instructions for use

1\. Run main.exe file, you can see the GUI interface along with a command console.

2\. Click 'step 1' tab, choose directories for MS files(RAW file), protein database (fasta file) and glycan branch structure database (13\_O\_glycan\_structures.xlsx，22\_O\_glycan\_structures.xlsx).

3\. Click 'step 2' tab, if you want to perform quantitative analysis, please select the corresponding label or click 'None' otherwise. Select fixed and variable modifications, if you need to add additional modifications, you can set modification name and monoisotopic mass by clicking 'Add to list' button.

4\. Click 'step 3' tab, fill in the search settings, such as energy, oxonium ions, mass tolerance peptide fragment number， peptide length and Max site number.

5\. Click 'Run' button to start search. Once it successfully starts, a page with progress bar(s) should appear within a few minutes.

6\. Result file will be generated in the same directory as the MS file after the searching finishes.





Demo

Instructions to run on data

1\. Run main.exe file.

2\. Click 'step 1' tab, choose directories for MS files(test.raw), protein database (test.fasta) and glycan branch structure database (13\_O\_glycan\_structures.xlsx).

3\. Click 'step 3' tab, click 'Run' button to start search.

Expected output

test.xlsx(result file), test.csv and test.log in the directory of test.raw.

Expected run time

about 9min





Noting

1\. Up to now, there are a total of 13 and 22 O-Glycan structures and we are devoted to achieve O-Glycan structure database independant searching for StrucOGP currently.

2\. Quantification analysis of glycopeptide by StrucOGP can use only TMT and iTRAQ, label free quantification will be supportd in later version.

3\. Low energy and High energy spectra were used for glycan structure and peptide identification respectively, if you want to analysis MS file with single energy, set the high and low energy to the same.

4\. Top\_n: high energy spectra top peaks number selected for further identification;

    Oxo\_top\_n, Oxo\_ess\_n, Oxo\_ess\_mz: glycopeptide spectra filter parameters, top n peaks must contain Oxo\_ess\_n times Oxo\_ess\_mz.

5\. StrucOGP is available freely for academic research, non-commercial or educational purposes under academic license.





Contact

If you have any questions or suggestions, please contact sun\_glycolab@126.com or post issues at Github(https://github.com/Sun-GlycoLab/StrucOGP).

