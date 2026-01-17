
import flash.Lib;

//import MyClip;

class Main {
	static function main() {
		var stage = Lib.current.stage;

		var shape = new MyClip();
		shape.x = (stage.stageWidth - 100) / 2;
		shape.y = (stage.stageHeight - 100) / 2;

		stage.addChild(shape);

//		var img = new Bitmap( new MyBitmapData(0, 0) );
//		Lib.current.addChild(img);
	}
}
