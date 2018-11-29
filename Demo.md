<!--
author:   Your Name
email:    your@email.com
version:  0.1.0
language: en
narrator: US English Female

comment:  This simple description of your course.
          Multiline is also okay.

link:     https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css

script:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js

translation: Français translations/French.md
-->

# LiaScript

## Multimedia

?[alt-text](https://bigsoundbank.com/UPLOAD/mp3/1068.mp3)

!?[alt-text](https://www.youtube.com/embed/bICfKRyKTwE)


## Code

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
<script>
  try{
    eval(`@input`);
  } catch (e) {
    var log = e.stack.match(/((.*?):(.*))\n.*?(:(\d+):(\d+)\)\n)/);
    var err_msg = new LiaError(log[1] + " =>  (" + log[4], 1);
    err_msg.add_detail(0, log[3], "error", log[5]-1, log[6]);
    throw err_msg;
  }
</script>

## Quizzes

[[ ]] Add as many elements as you want?
[[X]] The X marks the correct answer!
[[ ]] ... this is wrong ...
[[X]] ... this has to be selected too ...

## Diagrams

                                Multiline
1.9 |
    |                 ***
  y |               *     *
  - | r r r r r r r*r r r r*r r r r r r r
  a |             *         *
  x |            *           *
  i | B B B B B * B B B B B B * B B B B B
  s |         *                 *
    | *  * *                       * *  *
 -1 +------------------------------------
    0              x-axis               1
