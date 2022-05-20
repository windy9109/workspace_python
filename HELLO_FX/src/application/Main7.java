package application;

import java.util.ArrayList;
import java.util.List;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class Main7 extends Application {
	
	Button btn;
	TextField tf1;
	TextField tf2;
	TextArea ta;

	
	
	@Override
	public void start(Stage primaryStage) {
		try {

			Parent root = (Parent) FXMLLoader.load(getClass().getResource("main7.fxml"));
			Scene scene = new Scene(root, 400, 500);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());

			btn = (Button) scene.lookup("#btn");
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			ta = (TextArea) scene.lookup("#ta");

			
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick();
				}
			});
			
			primaryStage.setScene(scene);
			primaryStage.show();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	
	public void muclick() {
		int num1 = Integer.parseInt(tf1.getText());
		int num2 = Integer.parseInt(tf2.getText());
		String a = "";
		
		for(int i=num1; i<num2+1; i++) {
			for(int j=0; j<i; j++) {
				a += "*";
			}
			a += "\n";
		}
		
		ta.setText(a);
		
		
	}
	
	
	public static void main(String[] args) {
		launch(args);

	}

}
