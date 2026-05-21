
//3 i flash.Lib

/*3 class Main {
	static
	function main() {
		var stage = Lib.current.stage;
*/
		attachMovie('MyClip','shape',getNextHighestDepth());//3 var shape = new MyClip();
		shape._x = (Stage.width - 100) / 2;//3 shape.x = (stage.stageWidth - 100) / 2;
		shape._y = (Stage.height - 100) / 2;//3 shape.y = (stage.stageHeight - 100) / 2;
/*3
		stage.addChild(shape);

c		var img = new Bitmap( new MyBitmapData(0, 0) );
c		Lib.current.addChild(img);
	}
}

c import flash.display.BitmapData;
c import flash.display.Bitmap;
c @:bitmap('relative/path/to/myfile.png')
c class MyBitmapData extends BitmapData { }//*
*/
