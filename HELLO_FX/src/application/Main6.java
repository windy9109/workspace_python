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

public class Main6 extends Application {
	
	Button btn;
	Label lbl1;
	Label lbl2;
	Label lbl3;
	Label lbl4;
	Label lbl5;
	Label lbl6;
	
	
	@Override
	public void start(Stage primaryStage) {
		try {

			Parent root = (Parent) FXMLLoader.load(getClass().getResource("main6.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());

			btn = (Button) scene.lookup("#btn");
			lbl1 = (Label) scene.lookup("#lbl1");
			lbl2 = (Label) scene.lookup("#lbl2");
			lbl3 = (Label) scene.lookup("#lbl3");
			lbl4 = (Label) scene.lookup("#lbl4");
			lbl5 = (Label) scene.lookup("#lbl5");
			lbl6 = (Label) scene.lookup("#lbl6");
			
			
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
		int[] arr = new int[45];
		List<Integer> arr6 = new ArrayList<Integer>();
		for(int i=0; i<45; i++) {
			arr[i] = i;
		}
		
		
		while(true) {
			int random = (int)((Math.random()*45)+1);
			if( arr[random] == -1 ) {
				continue;
			}
			else {
				arr6.add(arr[random]);
					 arr[random] = -1;
			}
			if (arr6.size() >= 6) {
				break;
			}
			
		}
		
		
		lbl1.setText(Integer.toString(arr6.get(0)));
		lbl2.setText(Integer.toString(arr6.get(1)));
		lbl3.setText(Integer.toString(arr6.get(2)));
		lbl4.setText(Integer.toString(arr6.get(3)));
		lbl5.setText(Integer.toString(arr6.get(4)));
		lbl6.setText(Integer.toString(arr6.get(5)));
		
		
		
	}
	
	
	public static void main(String[] args) {
		launch(args);

	}

}
