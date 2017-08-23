/**
 * Created by shihan.ran on 2017/8/23.
 */

 function tryFindSimilar(text) {
        // 若都选择否，则返回undefined
        var text_core_strip_parentheses = stripUnimportantChars(text.replace(/(\(.+?\)|（(.+?)）|【(.+?)】|\[(.+?)\])/mg, ""));
        var text_core = stripUnimportantChars(text);
        var threshold = text_core.length * 0.22;
        for (var key in window.fdty_database) {
            if (!window.fdty_database.hasOwnProperty(key))
                continue;

            var possible = false;

            //尝试Levenshtein
            var LevenshteinDistance = new Levenshtein(text_core, key).distance;
            if (LevenshteinDistance <= threshold)
                possible = true;

            //尝试包含
            if (key.indexOf(text_core_strip_parentheses) >= 0)
                possible = true;

            if (possible) {
                if (confirm(text + '\n' + key + '\n这两题是否一样？')) {
                    return window.fdty_database[key];
                }
            }
        }
        return undefined;
    }