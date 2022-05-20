package application;



import com.sun.glass.ui.Screen;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.stage.Stage;

public class MainA extends Application {
	
	Button btn;
	TextField tf;
	TextArea ta;
	int a;
	int b;
	int c;
	
	@Override
	public void start(Stage primaryStage) {
		try {

			Parent root = (Parent) FXMLLoader.load(getClass().getResource("mainA.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());

			btn = (Button) scene.lookup("#btn");
			tf = (TextField) scene.lookup("#tf");
			ta = (TextArea) scene.lookup("#ta");
			
			
			
			a= (int)(Math.random()*9);
			b= (int)(Math.random()*9);
			c= (int)(Math.random()*9);
			
			while( a == b || a == c || b == c ) {
				a = (int)(Math.random()*9);
				b = (int)(Math.random()*9);
				c = (int)(Math.random()*9);
			}
		

			
			tf.setOnKeyPressed(new EventHandler<KeyEvent>() {

				@Override
				public void handle(KeyEvent event) {
					
					if(event.getCode() == KeyCode.ENTER) {
						muclick(a,b,c);
					}
					
					
				}
			});
			
			
			primaryStage.setScene(scene);
			primaryStage.show();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	
	public void muclick(int a, int b, int c) {
		
		
		int s1=0;
		int b1=0;
		

		int num = Integer.parseInt( tf.getText());
		
		int num1 = (int)(num/100); 
		int num2 = ((int)(num/10))%10; 
		int num3 = num%10;
		
		int[] number = { num1,num2,num3 };
		int[] com = { a,b,c };
		
		for(int i=0; i<number.length; i++) {
			for(int j=0; j<number.length; j++) {
				if( number[i] == com[j] && i == j) {
					s1++;
				}
				if( number[i] == com[j] && i != j) {
					b1++;
				}
			}
		}
		
		if(s1 == 3) {
			Alert alert = new Alert(AlertType.WARNING);
			alert.setTitle("Calling");
			alert.setHeaderText("모두 맞췄습니다! 축하합니다!");
			//alert.setContentText("Careful with the next step!");

			alert.showAndWait();
		}
		
		String str_new = "컴:"+a+b+c+", 나:"+num+" - S:"+s1+", B:"+b1+"\n";
		String str_old = ta.getText();
		
		ta.setText(str_old+str_new);
		tf.setText("");
		
		
		
	
		
				
	}
	
	
	public static void main(String[] args) {
		launch(args);

	}

}
