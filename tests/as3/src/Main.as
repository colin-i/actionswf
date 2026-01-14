
import flash.Lib;

import flash.display.Shape;
//import flash.display.BitmapData;
//import flash.display.Bitmap;

class Main {
	static function main() {
		var stage = Lib.current.stage;

		// create a center aligned rounded gray square
		var shape = new Shape();
		shape.graphics.beginFill(0x333333);
		shape.graphics.drawRoundRect(0, 0, 100, 100, 10);
		shape.x = (stage.stageWidth - 100) / 2;
		shape.y = (stage.stageHeight - 100) / 2;

		stage.addChild(shape);

//		var img = new Bitmap( new MyBitmapData(0, 0) );
//		Lib.current.addChild(img);
	}
}

//@:bitmap("/home/bc/games/tmp/0/back.png")
//class MyBitmapData extends BitmapData { }
