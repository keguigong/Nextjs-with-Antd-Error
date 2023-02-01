/**
 * N 字形变换
 * https://leetcode.cn/problems/zigzag-conversion/
 */

// 仅打印出字符串
function convert(s: string, numRows: number): string {
  let arr = new Array<string>(numRows);
  let pieceSize = numRows > 1 ? numRows * 2 - 2 : 1;

  for (let i = 0; i < s.length; i++) {
    let kthOfPiece = i % pieceSize;
    let y =
      kthOfPiece < numRows
        ? kthOfPiece
        : numRows - (kthOfPiece + 1 - (numRows - 1));

    arr.splice(y, 1, (arr[y] ? arr[y] : "") + s[i]);
  }

  return arr.join("");
}

// 按照ZigZag的形式打印出来
function convert1(s: string, numRows: number): string {
  let xyMap = new Map<number[], string>();
  let pieceSize = numRows > 1 ? numRows * 2 - 2 : 1;

  for (let i = 0; i < s.length; i++) {
    let kthPiece = Math.floor(i / pieceSize);
    let kthOfPiece = i % pieceSize;
    // console.log(kthPiece, kthOfPiece);

    let x =
      (numRows - 1) * kthPiece +
      (kthOfPiece < numRows ? 0 : kthOfPiece - numRows + 1);
    let y =
      kthOfPiece < numRows
        ? kthOfPiece
        : numRows - (kthOfPiece + 1 - (numRows - 1));

    xyMap.set([x, y], s[i]);
  }

  // console.log(xyMap);

  let x1 = -1;
  let outstr = "";
  for (let j = 0; j < numRows; j++) {
    let rowstr = "";
    xyMap.forEach((value, key, _) => {
      if (key[1] === j) {
        rowstr += new Array(key[0] - x1).join(" ") + value;
        x1 = key[0];
      }
    });
    x1 = -1;
    outstr += rowstr + "\n";
  }

  return outstr;
}

console.log(convert1("PAYPALISHIRING", 3));

// "PAYPALISHIRING", 3
// P A H N
// APLSIIG
// Y I R

// "PAYPALISHIRING", 
// P  I  N
// A LS IG
// YA HR
// P  I
