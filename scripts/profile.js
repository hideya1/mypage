"use strict";
//
const kw_p = document.getElementById("keywords_p");
let result = ""
for (const kw of Keywords) {
    result += kw[0] + ", "
};
result = result.slice(0,-2);
result += "."
kw_p.textContent = result;


let edu_ul = document.getElementById("edu_ul");
for (const obj of Education) {
    const li = document.createElement("li"),
    div1 = document.createElement("div"),
    div2 = document.createElement("div");
    div1.className = "b_2col_list_1st";
    div2.className = "b_2col_list_2nd";
    div1.textContent = `${obj.type[0]}:`;
    div2.innerHTML = `<a href="${obj.url[0]}">${obj.univ[0]}</a>, ${obj.date}, Supervisor: ${obj.advisor[0]}`;
    li.append(div1, div2);
    edu_ul.append(li);
};


let his_ul = document.getElementById("his_ul");
for (const obj of ResearchHistory) {
    let li = document.createElement("li"),
    div1 = document.createElement("div"),
    div2 = document.createElement("div");
    div1.className = "b_2col_list_1st";
    div2.className = "b_2col_list_2nd";
    div1.textContent = `${obj.from}${ENDASH}${obj.to}:`;
    div2.innerHTML = `<a href="${obj.url[0]}">${obj.at[0]}</a>, ${obj.as[0]}.`;
    li.append(div1, div2);
    his_ul.append(li);
};