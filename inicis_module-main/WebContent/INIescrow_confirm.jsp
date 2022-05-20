<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="EUC-KR"%>
<%@ page import="com.inicis.std.util.HttpUtil"%>
<%@ page import="java.text.SimpleDateFormat"%>
<%@ page import="com.inicis.std.util.SignatureUtil"%>
<%@ page import="java.util.*"%>
<%
	
	//############################################
	// 1.���� �ʵ� �� ����(***������ ���߼���***)
	//############################################

	// ���⿡ ������ ���� Form �ʵ忡 ������ ������ ����
	String mid				    = "iniescrow0";							            // ������ ID(������ ������ ����)					
	String signKey			  = "SU5JTElURV9UUklQTEVERVNfS0VZU1RS";		// �������� ������ �� ǥ�� ����Ű(������ ���� ������ ���������� �߱� ���� �� ����)
	String timestamp		  = SignatureUtil.getTimestamp();			    // util�� ���ؼ� �ڵ�����

	//###################################
	// 2. ������ Ȯ���� ���� signKey�� �ؽð����� ���� (SHA-256��� ���)
	//###################################
	String mKey = SignatureUtil.hash(signKey, "SHA-256");
	
	/* ��Ÿ */
	String siteDomain = ""; //������ ������ �Է�

%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style type="text/css">
	body { background-color: #efefef;}
	body, tr, td {font-size:9pt; font-family:����,verdana; color:#433F37; line-height:19px;}
	table, img {border:none}
</style>

<!-- �̴Ͻý� ǥ�ذ��� js  
     *****************************************************
     * �׽�Ʈ ���� �� URL : https://stgstdpay.inicis.com *
     * �ǿ ���� �� URL : https://stdpay.inicis.com    *
     *****************************************************
-->
<script language="javascript" type="text/javascript" src="https://stgstdpay.inicis.com/stdjs/INIStdPay_escrow_conf.js" charset="UTF-8"></script>

</head>
<body bgcolor="#FFFFFF" text="#242424" leftmargin=0 topmargin=15 marginwidth=0 marginheight=0 bottommargin=0 rightmargin=0>
	<div style="padding:10px;background-color:#f3f3f3;width:100%;font-size:13px;color: #ffffff;background-color: #000000;text-align: center">
		�̴Ͻý� ǥ�ذ��� ����ũ�� ���� Ȯ�� ����
	</div>
	<table width="650" border="0" cellspacing="0" cellpadding="0" style="padding:10px;" align="center">
		<tr>
			<td bgcolor="6095BC" align="center" style="padding:10px">
				<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" style="padding:20px">

					<tr>
						<td >
							<button onclick="INIStdPay.pay('SendPayForm_id')" style="padding:10px">����ũ�ΰŷ�Ȯ�ο�û</button>
						</td>
					</tr>
					<tr>
						<td>
							<table width="100%">
								<tr>
									<td style="text-align:left;">
										<form id="SendPayForm_id" name="" method="POST" >
											<!-- �ʼ� -->
											
											<div style="border:2px #dddddd double;padding:10px;background-color:#f3f3f3;">

												<b>�ŷ���ȣ(TID)</b>
												<input  style="width:100%;" name="tid" value="" >
												
												<!-- form ������ ������ �Ŵ��� ����  -->
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