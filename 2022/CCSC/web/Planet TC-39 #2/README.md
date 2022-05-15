# Planet TC-39 \#2

## Problem

[app.js](app.js)

## Solution

This is similar to [Planet TC-39 #1](../Planet%20TC-39%20%231/), but now there is a check that the 2 values should be safe integers. So, my previous solution of using identical strings does not work here.

I was able to find a solution: `var a = 0` and `var b = -0`. `0 === -0` is `true`, but `1/0 === 1/-0` is `false` since `Infinity === -Infinity` is `false`.
