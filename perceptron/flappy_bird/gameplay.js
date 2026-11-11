window.onload = function() {
	startGame();
}

function startGame(){	
	let game = new Phaser.Game(640, 360, Phaser.CANVAS, 'game');

	game.state.add('Main', App.main);
	game.state.start('Main');
}

let App = {};

App.Main = function(game){
	this.STATE_INIT = 1;
	this.STATE_START = 2;
	this.STATE_PLAY = 3;
	this.STATE_GAMEOVER = 4;

	this.BARRIER_DISTANCE = 300;
}

App.Main.prototype = {
	preload : function(){
		loadSpriteSheets(this.game);
		loadGameImages(this.game);
		loadBitMapFonts(this);
	}
}

function loadSpriteSheets(game){
	game.load.spritesheet('imgBird', 'assets/img_bird.png', 18, 18, 10);
	game.load.spritesheet('imgTree', 'assets/img_tree.png', 45, 200, 1);
	game.load.spritesheet('ImgButtons', 'assets/img_buttons.png', 55, 20, 1.5);
}

function loadGameImages(game){
	game.load.image('imgTarget', 'assets/img_target.png');	
	game.load.image('imgGround', 'assets/img_ground.png');
	game.load.image('imgPause', 'assets/img_pause.png');
	game.load.image('imgTarget', 'assets/img_target.png');
}

function loadBitMapFonts(main){
	main.load
}
