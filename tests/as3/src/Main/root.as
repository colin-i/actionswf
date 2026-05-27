
//3 i flash.Lib

/*3 a Main
	f s
		g stage
*/
		attachMovie('MyClip','shape',getNextHighestDepth());//3 v shape MyClip
		shape._x = (Stage.width - 100) / 2;//3 s
		shape._y = (Stage.height - 100) / 2;//3 s
		/*3 d shape stage

c		var img = new Bitmap( new MyBitmapData(0, 0) );
c		Lib.current.addChild(img);
	}
}

c import flash.display.BitmapData;
c import flash.display.Bitmap;
c @:bitmap('relative/path/to/myfile.png')
c class MyBitmapData extends BitmapData { }//*
*/
