package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class Main3 extends Application {
	
	Button btn;
	TextField tf1;
	TextField tf2;
	TextField tf3;
	Label lbl;
	
	
	@Override
	public void start(Stage primaryStage) {
		try {

			Parent root = (Parent) FXMLLoader.load(getClass().getResource("main3.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			btn = (Button) scene.lookup("#btn");
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			tf3 = (TextField) scene.lookup("#tf3");
			lbl = (Label) scene.lookup("#lbl");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					muclick();
				}
			});
			
			
//			if(!tf1.getText().equals("") && !tf2.getText().equals("")) {
//				int sum = Integer.parseInt(tf1.getText()) + Integer.parseInt(tf2.getText()); 
//				tf3.setText(Integer.toString(sum));
//			}else {
//				tf3.setText("연산할수없습니다.");
//			}
			
			primaryStage.setScene(scene);
			primaryStage.show();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	
	public void muclick() {
		String a = tf1.getText();
		String b = tf2.getText();
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		int sum = aa+bb;
		tf3.setText(Integer.toString(sum));
	}
	
	
	public static void main(String[] args) {
		launch(args);

	}

}
