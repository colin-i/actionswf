
/*3 i flash.display.MovieClip
i flash.display.Shape
i flash.events.Event
i flash.text.TextField
i flash.text.TextFormat
i flash.text.TextFormatAlign
i flash.events.MouseEvent

a MyClip MovieClip*/
	function on_Enter_Frame(){//3 e
		if(a){
			_x-=c;//3 s _
			if(b){
				_y-=c;//3 s _
				if(_y<=0){//3 s _
					b=false;
				}
			}else{
				_y+=c;//3 s _
				if(_y+_height>=Stage.height){//3 s _h
					b=true;
				}
			}
			if(_x<=0){//3 s _
				a=false;
			}
		}else{
			_x+=c;//3 s _
			if(b){
				_y-=c;//3 s _
				if(_y<=0){//3 s _
					b=false;
				}
			}else{
				_y+=c;//3 s _
				if(_y+_height>=Stage.height){//3 s _h
					b=true;
				}
			}
			if(_x+_width>=Stage.width){//3 s _w
				a=true;
			}
		}
	}
	// Handlers
	function onClick(){//3 e
		trace('Button clicked!');
	}
	function onOver(){//3 e
		_alpha = 80;//3 alpha = 0.8;
	}
	function onOut(){//3 e
		_alpha = 100;//3 alpha = 1;
	}
/*3
	f pnew
		super();
*/
		// Simple visual so you can see it
		//3 var shape = new Shape();
		beginFill(0x3399FF);//3 shape.graphics.beginFill(0x3399FF);
		lineTo(120, 0);lineTo(120, 80);lineTo(0, 80);//3 shape.graphics.drawRect(0, 0, 120, 80);
		endFill();//3 shape.graphics.endFill();
		//3 addChild(shape);

		// a 1/5 margin
		createTextField('label',1,0,16, 120, 48);//3 t
		label.text = 'Click';
		label.selectable = false;

		// a 2/3 size format
		var tf = new TextFormat();
		tf.size = 32;
		tf.align = 'center';//3 tf.align = TextFormatAlign.CENTER;
		tf.color = 0xff9933;
		label.setTextFormat(tf);

		// Interactivity
		useHandCursor = true;//3 buttonMode = true;mouseChildren = false;
		onRollOver = onOver;//3 o
		onRollOut = onOut;//3 o
		onPress = onClick;//3 o

		//3 addChild(label);

		onEnterFrame = on_Enter_Frame; //3 o
/*3	}
	static
*/
	var c=%u;
	var a=false;var b=false;
//3 }
