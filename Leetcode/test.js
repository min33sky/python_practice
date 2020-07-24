let str = 'h1h1x`3 abc def';

console.log(str.replace(/^(\S+)\s(.*)/, '$2$1'));
