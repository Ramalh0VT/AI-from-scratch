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

}
