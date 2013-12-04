Array.prototype.pick = function() {
  return this[Math.floor(Math.random()*this.length)];
};

var el = $('#content');

function generate() {
  el.text(skills.pick());
  el.fadeIn(2000, function() {
    el.fadeOut(2000, function() {
      generate();
    });
  });
}

generate();
