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
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.stage.Stage;

public class Main4 extends Application {
	
	Button btn;
	TextField tf1;
	TextField tf2;
	TextField tf3;
	
	
	@Override
	public void start(Stage primaryStage) {
		try {

			Parent root = (Parent) FXMLLoader.load(getClass().getResource("main4.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());

			btn = (Button) scene.lookup("#btn");
			tf1 = (TextField) scene.lookup("#tfMine");
			tf2 = (TextField) scene.lookup("#tfCom");
			tf3 = (TextField) scene.lookup("#tfResult");
			
			
		

			
			tf1.setOnKeyPressed(new EventHandler<KeyEvent>() {

				@Override
				public void handle(KeyEvent event) {
					//System.out.println(event.getCode());
					
//					if(event.getCode().toString().equals("ENTER")) {
//						System.out.println("참");
//					}
					
					if(event.getCode() == KeyCode.ENTER) {
						muclick();
					}
					
					
				}
			});
			
			
			primaryStage.setScene(scene);
			primaryStage.show();

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	
	public void muclick() {
		int a = (int)(Math.random()*10);
		if( a >= 7 ) { tf2.setText("가위"); }
		else if( a >= 3 ) { tf2.setText("바위"); }
		else { tf2.setText("보"); }
		
		if( tf2.getText().equals("가위") && tf1.getText().equals("바위") || tf2.getText().equals("바위") && tf1.getText().equals("보") || tf2.getText().equals("보") && tf1.getText().equals("가위") ) {
			tf3.setText("당신이 이겼습니다.");
		}else if( tf2.getText().equals(tf1.getText())) {
			tf3.setText("비겼습니다.");
		}else{
			tf3.setText("졌습니다.");
		}
		
				
	}
	
	
	public static void main(String[] args) {
		launch(args);

	}

}
