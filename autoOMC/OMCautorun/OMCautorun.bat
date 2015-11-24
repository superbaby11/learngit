set Receiver=wangwh@nco-china.com.cn,475663574@qq.com

::run testcase
python -m robot.run --suite DefaultConfiguration --outputdir D:\OMCoutput D:\OMCTest

::generate output
python D:\OMCoutput\robot\rebot.py --summary summary.html --log NONE --report NONE --outputdir D:\OMCoutput D:\OMCoutput\output.xml

::send mail
python D:\OMCsendmail\sendmail.py D:\OMCoutput\summary.html D:\OMCoutput\report.html %Receiver%