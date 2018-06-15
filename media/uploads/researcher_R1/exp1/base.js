// function to calculate the result of the survey
  var tbl = {"q1": "", "q2":"", "q3":"", "q4":"","ans":""}
function tabulateAnswers() {
  // initialize variables for each choice's score
  // If you add more choices and outcomes, you must add another variable here.
  var c1score = 0;
  var c2score = 0;
  var c3score = 0;
  var c4score = 0;
  var q = [];
  var ans;
  // get a list of the radio inputs on the page
  var choices = document.getElementsByTagName('input');
  // loop through all the radio inputs
  for (i=0; i<choices.length; i++) {
    // if the radio is checked..
    if (choices[i].checked) {
      // add 1 to that choice's score
      if (choices[i].value == 'c1') {
        c1score = c1score + 1;
        ans = 'c1'
      }
      if (choices[i].value == 'c2') {
        c2score = c2score + 1;
        ans = 'c2'
      }
      if (choices[i].value == 'c3') {
        c3score = c3score + 1;
        ans = 'c3'
      }
      if (choices[i].value == 'c4') {
        c4score = c4score + 1;
        ans = 'c4'
      }
      q.push(ans);
      // If you add more choices and outcomes, you must add another if statement below.
    }
  }
  
  // Find out which choice got the highest score.
  // If you add more choices and outcomes, you must add the variable here.
  var maxscore = Math.max(c1score,c2score,c3score,c4score);
  var C1 = "You are a computer researcher! You will enjoy developing algorithms, and doing things with computers no one else has done before. For example, researchers sent a robot to the moon, built a computer to beat the best humans in Jeopardy, and are creating robots to do your chores for you. Computer researchers typically go to college and work at universities, or as a part of the research and development team in companies.";
  var C2 = "You are an altruistic coder! You love to help people and feel the positive impact of your work every day. Altrustic coders are out there every day making the world a better place. Computer scientists write software to more effectively help doctors diagnose illnesses such as cancer, connect people in third world countries to education and medical resources on the internet, code websites and software for nonprofit organizations, and much more!";
  var C3 = "You are a developer! Developers create games, apps, social media, movies, and all sorts of fun programs that people enjoy. These coders work on projects such as Minecraft, Poptropica, and Youtube. Developers need sharp coding skills, are great debuggers, and need to work well in a team of other developers.";
  var C4 = "You are the future CEO of a new startup! You enjoy taking risks and building the next big thing that no one has even thought of before. For example, billionare Mark Zuckerberg founded Facebook in 2004, a project he started inside his dorm room in college which eventually turned into a social networking revolution that changed the world.";

  // Display answer corresponding to that choice
  var answerbox = document.getElementById('answer');
  if (c1score == maxscore) { // If user chooses the first choice the most, this outcome will be displayed.
    answerbox.innerHTML = C1;
    ans = C1;
    q.push("c1");
    
  }
  if (c2score == maxscore) { // If user chooses the second choice the most, this outcome will be displayed.
    answerbox.innerHTML = C2;
    ans = C2;
    q.push("c2");
  }
  if (c3score == maxscore) { // If user chooses the third choice the most, this outcome will be displayed.
    answerbox.innerHTML = C3;
    ans = C3;
    q.push("c3");
  }
  if (c4score == maxscore) { // If user chooses the fourth choice the most, this outcome will be displayed.
    answerbox.innerHTML = C4;
    ans = C4;
    q.push("c4");
  }
  // If you add more choices, you must add another response below.
  var i = 0;
 for (x in tbl) {
	 tbl[x] = q[i];
	 i++;
 }
  console.log(tbl);
  
}

// program the reset button
function resetAnswer() {
  var answerbox = document.getElementById('answer');
  answerbox.innerHTML = "Your result will show up here!";
}

function PostAnswer() {
	
	parent.PostData(tbl);
	
}