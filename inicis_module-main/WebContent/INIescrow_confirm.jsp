<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="EUC-KR"%>
<%@ page import="com.inicis.std.util.HttpUtil"%>
<%@ page import="java.text.SimpleDateFormat"%>
<%@ page import="com.inicis.std.util.SignatureUtil"%>
<%@ page import="java.util.*"%>
<%
	
	//############################################
	// 1.전문 필드 값 설정(***가맹점 개발수정***)
	//############################################

	// 여기에 설정된 값은 Form 필드에 동일한 값으로 설정
	String mid				    = "iniescrow0";							            // 가맹점 ID(가맹점 수정후 고정)					
	String signKey			  = "SU5JTElURV9UUklQTEVERVNfS0VZU1RS";		// 가맹점에 제공된 웹 표준 사인키(가맹점 상점 관리자 페이지에서 발급 받은 후 고정)
	String timestamp		  = SignatureUtil.getTimestamp();			    // util에 의해서 자동생성

	//###################################
	// 2. 가맹점 확인을 위한 signKey를 해시값으로 변경 (SHA-256방식 사용)
	//###################################
	String mKey = SignatureUtil.hash(signKey, "SHA-256");
	
	/* 기타 */
	String siteDomain = ""; //가맹점 도메인 입력

%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style type="text/css">
	body { background-color: #efefef;}
	body, tr, td {font-size:9pt; font-family:굴림,verdana; color:#433F37; line-height:19px;}
	table, img {border:none}
</style>

<!-- 이니시스 표준결제 js  
     *****************************************************
     * 테스트 연동 시 URL : https://stgstdpay.inicis.com *
     * 실운영 연동 시 URL : https://stdpay.inicis.com    *
     *****************************************************
-->
<script language="javascript" type="text/javascript" src="https://stgstdpay.inicis.com/stdjs/INIStdPay_escrow_conf.js" charset="UTF-8"></script>

</head>
<body bgcolor="#FFFFFF" text="#242424" leftmargin=0 topmargin=15 marginwidth=0 marginheight=0 bottommargin=0 rightmargin=0>
	<div style="padding:10px;background-color:#f3f3f3;width:100%;font-size:13px;color: #ffffff;background-color: #000000;text-align: center">
		이니시스 표준결제 에스크로 구매 확정 샘플
	</div>
	<table width="650" border="0" cellspacing="0" cellpadding="0" style="padding:10px;" align="center">
		<tr>
			<td bgcolor="6095BC" align="center" style="padding:10px">
				<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" style="padding:20px">

					<tr>
						<td >
							<button onclick="INIStdPay.pay('SendPayForm_id')" style="padding:10px">에스크로거래확인요청</button>
						</td>
					</tr>
					<tr>
						<td>
							<table width="100%">
								<tr>
									<td style="text-align:left;">
										<form id="SendPayForm_id" name="" method="POST" >
											<!-- 필수 -->
											
											<div style="border:2px #dddddd double;padding:10px;background-color:#f3f3f3;">

												<b>거래번호(TID)</b>
												<input  style="width:100%;" name="tid" value="" >
												
												<!-- form 데이터 설명은 매뉴얼 참조  -->
												<input type="hidden" name="version" 	value="1.0" >
												<input type="hidden" name="mid" 		value="<%=mid%>" >
												<input type="hidden" name="currency" 	value="WON" >
												<!-- payViewType defalut value = overlay -->
												<input type="hidden" name="payViewType" value="" >
												<!-- charset defalut value = UTF-8 -->
												<input type="hidden" name="charset" 	value="EUC-KR" >
												<input type="hidden" name="timestamp" 	value="<%=timestamp %>" >
												<input type="hidden" name="mKey"		value="<%=mKey%>" >		
												<input type="hidden" name="returnUrl"	value="<%=siteDomain%>/INIescrow_confirm_return.jsp" >																						
												<input type="hidden" name="closeUrl" 	value="<%=siteDomain%>/close.jsp" >
												<input type="hidden" name="popupUrl" 	value="<%=siteDomain%>/popup.jsp" >
											</div>
										</form>
									</td>
								</tr>
							</table>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
	
</body>
</html>