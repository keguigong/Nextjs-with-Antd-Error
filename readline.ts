const readline = require("readline")

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.setPrompt("> Please enter 2 number, seperated by space\r\n")
rl.prompt()

rl.on("line", (line) => {
  const tokens = line.split(" ")
  console.log(parseInt(tokens[0]) + parseInt(tokens[1]))
})
