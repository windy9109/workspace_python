<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="EUC-KR"%>
<%@ page import="java.util.*"%>
<%@ page import="com.inicis.std.util.SignatureUtil"%>
<%@ page import="com.inicis.std.util.HttpUtil"%>
<% 

		//#############################
		// 인증결과 파라미터 일괄 수신
		//#############################
    
    //가맹점 인코딩에 맞게 설정(한글 깨질경우)
    request.setCharacterEncoding("EUC-KR");
    
		Map<String,String> paramMap = new Hashtable<String,String>();

		Enumeration elems = request.getParameterNames();

		String temp = "";

		while(elems.hasMoreElements())
		{
			temp = (String) elems.nextElement();
			//paramMap.put(temp, new String(((String)request.getParameter(temp)).getBytes("ISO-8859-1"),"UTF-8"));
			paramMap.put(temp, request.getParameter(temp));
		}

		System.out.println("paramMap : "+ paramMap.toString());

		String tid          = paramMap.get("tid"); 					    // 거래번호
		String resultCode   = paramMap.get("ResultCode");			  // 결과코드 ("00"이면 지불 성공)
		String resultMsg    = paramMap.get("ResultMsg");    		// 결과내용 (결과에 대한 설명)
		String resultDate   = paramMap.get("CNF_Date");    			// 구매확정 처리 날짜
		String resultTime   = paramMap.get("CNF_Time");    			// 구매확정 처리 시각
		
		//구매 거절 시
		if(paramMap.get("DNY_Date") != null){
			resultDate   = paramMap.get("DNY_Date");              // 구매거절 처리 날짜
			resultTime   = paramMap.get("DNY_Time");              // 구매거절 처리 시각
		}
		
%>
<html>
<head>
<title>INIescrow 구매확인 결과</title>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<link rel="stylesheet" href="css/group.css" type="text/css">
<style>
body, tr, td {font-size:9pt; font-family:굴림,verdana; color:#433F37; line-height:19px;}
table, img {border:none}

/* Padding ******/ 
.pl_01 {padding:1 10 0 10; line-height:19px;}
.pl_03 {font-size:20pt; font-family:굴림,verdana; color:#FFFFFF; line-height:29px;}

/* Link ******/ 
.a:link          {font-size:9pt; color:#333333; text-decoration:none}
.a:visited       {font-size:9pt; color:#333333; text-decoration:none}
.a:hover         {font-size:9pt; color:#0174CD; text-decoration:underline}

.txt_03a:link    {font-size: 8pt;line-height:18px;color:#333333; text-decoration:none}
.txt_03a:visited {font-size: 8pt;line-height:18px;color:#333333; text-decoration:none}
.txt_03a:hover   {font-size: 8pt;line-height:18px;color:#EC5900; text-decoration:underline}
</style>

<script language="JavaScript" type="text/JavaScript">
<!--
function MM_reloadPage(init) {  //reloads the window if Nav4 resized
  if (init==true) with (navigator) {if ((appName=="Netscape")&&(parseInt(appVersion)==4)) {
    document.MM_pgW=innerWidth; document.MM_pgH=innerHeight; onresize=MM_reloadPage; }}
  else if (innerWidth!=document.MM_pgW || innerHeight!=document.MM_pgH) location.reload();
}
MM_reloadPage(true);
//-->
</script>
</head>
<body bgcolor="#FFFFFF" text="#242424" leftmargin=0 topmargin=15 marginwidth=0 marginheight=0 bottommargin=0 rightmargin=0><center> 
<table width="632" border="0" cellspacing="0" cellpadding="0">
  <tr> 
    <td height="83" background="img/spool_top.gif"style="padding:0 0 0 64">
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td width="3%" valign="top"><img src="img/title_01.gif" width="8" height="27" vspace="5"></td>
          <td width="97%" height="40" class="pl_03"><font color="#FFFFFF"><b>에스크로 구매확인 결과</b></font></td>
        </tr>
      </table></td>
  </tr>
  <tr> 
    <td align="center" bgcolor="6095BC"><table width="620" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td bgcolor="#FFFFFF" style="padding:0 0 0 56">
		  <table width="510" border="0" cellspacing="0" cellpadding="0">
              <tr> 
                <td width="7"><img src="img/life.gif" width="7" height="30"></td>
                <td background="img/center.gif"><img src="img/icon03.gif" width="12" height="10"> 
                  <b>고객님께서 이니에스크로를 통해 구매확인 결과내용입니다. </b></td>
                <td width="8"><img src="img/right.gif" width="8" height="30"></td>
              </tr>
            </table>
            <br>
            <table width="510" border="0" cellspacing="0" cellpadding="0">
              <tr> 
                <td width="407"  style="padding:0 0 0 9"><img src="img/icon.gif" width="10" height="11"> 
                  <strong><font color="433F37">구매확인 내역</font></strong></td>
                <td width="103">&nbsp;</td>
              </tr>
              <tr> 
                <td colspan="2"  style="padding:0 0 0 23">
		  <table width="470" border="0" cellspacing="0" cellpadding="0">
                    
                    <tr> 
                      <td width="18" align="center"><img src="img/icon02.gif" width="7" height="7"></td>
                      <td width="109" height="26">결 과 코 드</td>
                      <td width="343"><%=resultCode%></td>
                    </tr>
                    <tr> 
                      <td height="1" colspan="3" align="center"  background="img/line.gif"></td>
                    </tr>
                    <tr> 
                      <td width="18" align="center"><img src="img/icon02.gif" width="7" height="7"></td>
                      <td width="120" height="25">결 과 내 용</td>
                      <td width="330"><%=resultMsg%></td>
                    </tr>
                    <tr> 
                      <td height="1" colspan="3" align="center"  background="img/line.gif"></td>
                    </tr>
                    <tr> 
                      <td width='18' align='center'><img src='img/icon02.gif' width='7' height='7'></td>
                      <td width='120' height='25'>처리날짜(YYYYMMDD)</td>
                      <td width='330'><%=resultDate%></td>
                    </tr>                	    
                    <tr> 
                      <td height='1' colspan='3' align='center'  background='img/line.gif'></td>
                    </tr>
                    <tr> 
                      <td width='18' align='center'><img src='img/icon02.gif' width='7' height='7'></td>
                      <td width='120' height='25'>처리시각(hhmmss)</td>
                      <td width='330'><%=resultTime%></td>
                    </tr>
                    <tr> 
                      <td height='1' colspan='3' align='center'  background='img/line.gif'></td>
                    </tr>
                    
                    
                  </table></td>
              </tr>
            </table>
            <br>
           </td>
        </tr>
      </table></td>
  </tr>
    <td><img src="img/bottom01.gif" width="632" height="13"></td>
  </tr>
</table>
</center></body>
</html>
