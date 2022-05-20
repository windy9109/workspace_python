package application;

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

public class Main5 extends Application {
	
	Button btn;
	TextField tf_dan;
	TextArea ta;
	
	
	@Override
	public void start(Stage primaryStage) {
		try {

			Parent root = (Parent) FXMLLoader.load(getClass().getResource("main5.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());

			btn = (Button) scene.lookup("#btn");
			tf_dan = (TextField) scene.lookup("#tf_Dan");
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
		int dan = Integer.parseInt(tf_dan.getText());
		String b="";
		for(int i=0; i<9; i++){
			b += Integer.toString(i+1)+"*"+Integer.toString(dan)+"="+Integer.toString((i+1)*dan);
			b +="\n";
		}
		
		
		ta.setText(b);
		

				
	}
	
	
	public static void main(String[] args) {
		launch(args);

	}

}
