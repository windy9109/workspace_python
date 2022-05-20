package application;

import java.util.ArrayList;
import java.util.List;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class Main8_2 extends Application {
	
	Button btn_call;
	TextField tf;
	Button btn1;
	Button btn2;
	Button btn3;
	Button btn4;
	Button btn5;
	Button btn6;
	Button btn7;
	Button btn8;
	Button btn9;
	Button btn0;
	String a = "";
	
	@Override
	public void start(Stage primaryStage) {
		try {

			Parent root = (Parent) FXMLLoader.load(getClass().getResource("main8.fxml"));
			Scene scene = new Scene(root, 400, 500);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());

			tf = (TextField) scene.lookup("#tf");
			btn_call = (Button) scene.lookup("#btn_call");
			btn1 = (Button) scene.lookup("#btn1");
			btn2 = (Button) scene.lookup("#btn2");
			btn3 = (Button) scene.lookup("#btn3");
			btn4 = (Button) scene.lookup("#btn4");
			btn5 = (Button) scene.lookup("#btn5");
			btn6 = (Button) scene.lookup("#btn6");
			btn7 = (Button) scene.lookup("#btn7");
			btn8 = (Button) scene.lookup("#btn8");
			btn9 = (Button) scene.lookup("#btn9");
			btn0 = (Button) scene.lookup("#btn0");
			

			
			btn1.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick(event);
				}
				
			});
			
			btn2.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick(event);
				}
				
			});
			
			
			btn3.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick(event);
				}
				
			});
			
			btn4.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick(event);
				}
				
			});
			
			
			btn5.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick(event);
				}
				
			});
			
			
			btn6.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick(event);
				}
				
			});
			
			btn7.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick(event);
				}
				
			});
			
			
			btn8.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick(event);
				}
				
			});
			
			btn9.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick(event);
				}
				
			});
			
			
			btn0.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick(event);
				}
				
			});
			
			
			btn_call.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					mucall();
				}
				
			});
			
			
			
			primaryStage.setScene(scene);
			primaryStage.show();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	
	
	
	
	public void muclick(Event event) {
		
		
		
		Button imsi = (Button)event.getSource();
		String str_new = imsi.getText();
		String str_old= tf.getText();
		tf.setText(str_old+str_new);
	
		
	}
	
	
	
	
	public void mucall() {
		

		
		
		Alert alert = new Alert(AlertType.WARNING);
		alert.setTitle("Calling");
		alert.setHeaderText("Calling \n "+tf.getText());
		alert.setContentText("Careful with the next step!");

		alert.showAndWait();
	
		
	}



	

	

	

	
	
	public static void main(String[] args) {
		launch(args);

	}

}
