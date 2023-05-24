function generateRoutine() {
    var form_container = document.createElement("div");
    form_container.className = "container-fluid"
    form_container.appendChild(document.createElement("hr"));

    // 1> 事务名称
    var name_item = document.createElement("p");
    name_item.innerText = "事务名称";
    var name_text = document.createElement("input");
    name_text.type = "text";
    name_text.name = "name_text";

    form_container.appendChild(name_item);
    form_container.appendChild(name_text);
    form_container.appendChild(document.createElement("br"));
    form_container.appendChild(document.createElement("hr"));

    // 2> 周期 或 每周的哪一天
    var period_item = document.createElement("p");
    period_item.innerText = "周期";

    var period_slider = document.createElement("input");
    period_slider.type = "range";
    period_slider.id = "period";
    period_slider.min = 1;
    period_slider.max = 30;
    period_slider.name = "period_slider";

    var period_label = document.createElement("span");
    period_slider.addEventListener('input', function() {
        period_label.innerText = " " + period_slider.value + "天";
    });
    period_label.innerText = " " + period_slider.value + "天";
    period_label.setAttribute("for", "period");

    form_container.appendChild(period_item);
    form_container.appendChild(period_slider);
    form_container.appendChild(period_label);
    form_container.appendChild(document.createElement("hr"));

    // 4> 重要程度值
    var crucial_item = document.createElement("p");
    crucial_item.innerText = "重要程度值";

    var crucial_slider = document.createElement("input");
    crucial_slider.type = "range";
    crucial_slider.id = "crucial";
    crucial_slider.min = 1;
    crucial_slider.max = 10;
    crucial_slider.name = "crucial_slider";

    var crucial_label = document.createElement("span");
    crucial_slider.addEventListener('input', function() {
        crucial_label.innerText = " " + crucial_slider.value;
    });
    crucial_label.innerText = " " + crucial_slider.value;
    crucial_label.setAttribute("for", "crucial");

    form_container.appendChild(crucial_item);
    form_container.appendChild(crucial_slider);
    form_container.appendChild(crucial_label);
    form_container.appendChild(document.createElement("hr"));

    // 5> 提醒周期
    var remind_item = document.createElement("p");
    remind_item.innerText = "提醒周期";

    var remind_slider = document.createElement("input");
    remind_slider.type = "range";
    remind_slider.id = "crucial";
    remind_slider.min = 1;
    remind_slider.max = 10;
    remind_slider.name = "remind_slider";

    var remind_label = document.createElement("span");
    remind_slider.addEventListener('input', function() {
        remind_label.innerText = " " + remind_slider.value + "天";
    });
    remind_label.innerText = " " + remind_slider.value + "天";
    remind_label.setAttribute("for", "remind");

    form_container.appendChild(remind_item);
    form_container.appendChild(remind_slider);
    form_container.appendChild(remind_label);
    form_container.appendChild(document.createElement("hr"));

    // 6> 总进度值
    var progress_item = document.createElement("p");
    progress_item.innerText = "总进度值";

    var progress_slider = document.createElement("input");
    progress_slider.type = "range";
    progress_slider.id = "progress";
    progress_slider.min = 1;
    progress_slider.max = 100;
    progress_slider.name = "progress_slider";

    var progress_label = document.createElement("span");
    progress_slider.addEventListener('input', function() {
        progress_label.innerText = " " + progress_slider.value;
    });
    progress_label.innerText = " " + progress_slider.value;
    progress_label.setAttribute("for", "progress");

    form_container.appendChild(progress_item);
    form_container.appendChild(progress_slider);
    form_container.appendChild(progress_label);
    form_container.appendChild(document.createElement("hr"));

    // 7> 备注
    var remark_item = document.createElement("p");
    remark_item.innerText = "备注";
    var remark_text = document.createElement("input");
    remark_text.type = "text";
    remark_text.name = "remark_text"

    form_container.appendChild(remark_item);
    form_container.appendChild(remark_text);
    form_container.appendChild(document.createElement("br"));
    form_container.appendChild(document.createElement("hr"));

    return form_container;
}

function generateTemporary() {
    var form_container = document.createElement("div");
    form_container.className = "container-fluid"
    form_container.appendChild(document.createElement("hr"));

    // 1> 事务名称
    var name_item = document.createElement("p");
    name_item.innerText = "事务名称";
    var name_text = document.createElement("input");
    name_text.type = "text";
    name_text.name = "name_text";

    form_container.appendChild(name_item);
    form_container.appendChild(name_text);
    form_container.appendChild(document.createElement("br"));
    form_container.appendChild(document.createElement("hr"));

    // 2> 时限
    var limit_item = document.createElement("p");
    limit_item.innerText = "时限";

    var limit_hour_slider = document.createElement("input");
    limit_hour_slider.type = "range";
    limit_hour_slider.id = "limit_hour";
    limit_hour_slider.min = 0;
    limit_hour_slider.max = 23;
    limit_hour_slider.name = "limit_hour_slider";

    var limit_hour_label = document.createElement("span");
    limit_hour_slider.addEventListener('input', function() {
        limit_hour_label.innerText = " " + limit_hour_slider.value + "小时";
    });
    limit_hour_label.innerText = " " + limit_hour_slider.value + "小时";
    limit_hour_label.setAttribute("for", "limit_hour");

    var limit_day_slider = document.createElement("input");
    limit_day_slider.type = "range";
    limit_day_slider.id = "limit_day";
    limit_day_slider.min = 0;
    limit_day_slider.max = 100;
    limit_day_slider.name = "limit_day_slider";

    var limit_day_label = document.createElement("span");
    limit_day_slider.addEventListener('input', function() {
        limit_day_label.innerText = " " + limit_day_slider.value + "天";
    });
    limit_day_label.innerText = " " + limit_day_slider.value + "天";
    limit_day_label.setAttribute("for", "limit_day");

    form_container.appendChild(limit_item);
    form_container.appendChild(limit_hour_slider);
    form_container.appendChild(limit_hour_label);
    form_container.appendChild(document.createElement("br"));
    form_container.appendChild(limit_day_slider);
    form_container.appendChild(limit_day_label);
    form_container.appendChild(document.createElement("hr"));

    // 3> 重要程度值
    var crucial_item = document.createElement("p");
    crucial_item.innerText = "重要程度值";

    var crucial_slider = document.createElement("input");
    crucial_slider.type = "range";
    crucial_slider.id = "crucial";
    crucial_slider.min = 1;
    crucial_slider.max = 10;
    crucial_slider.name = "crucial_slider";

    var crucial_label = document.createElement("span");
    crucial_slider.addEventListener('input', function() {
        crucial_label.innerText = " " + crucial_slider.value;
    });
    crucial_label.innerText = " " + crucial_slider.value;
    crucial_label.setAttribute("for", "crucial");

    form_container.appendChild(crucial_item);
    form_container.appendChild(crucial_slider);
    form_container.appendChild(crucial_label);
    form_container.appendChild(document.createElement("hr"));

    // 4> 提醒周期
    var remind_item = document.createElement("p");
    remind_item.innerText = "提醒周期";

    var remind_slider = document.createElement("input");
    remind_slider.type = "range";
    remind_slider.id = "crucial";
    remind_slider.min = 1;
    remind_slider.max = 10;
    remind_slider.name = "remind_slider";

    var remind_label = document.createElement("span");
    remind_slider.addEventListener('input', function() {
        remind_label.innerText = " " + remind_slider.value + "天";
    });
    remind_label.innerText = " " + remind_slider.value + "天";
    remind_label.setAttribute("for", "remind");

    form_container.appendChild(remind_item);
    form_container.appendChild(remind_slider);
    form_container.appendChild(remind_label);
    form_container.appendChild(document.createElement("hr"));

    // 5> 备注
    var remark_item = document.createElement("p");
    remark_item.innerText = "备注";
    var remark_text = document.createElement("input");
    remark_text.type = "text";
    remark_text.name = "remark_text";

    form_container.appendChild(remark_item);
    form_container.appendChild(remark_text);
    form_container.appendChild(document.createElement("br"));
    form_container.appendChild(document.createElement("hr"));

    return form_container;
}

function generateDisplayWidgets(title, dct_id){
    var display_dct_string = document.getElementById(dct_id).getAttribute("data-dict");
//    display_dct_string.replace()
    var display_container = document.createElement("div");
    display_container.className = "container-fluid"

    var title_item = document.createElement("p");
    title_item.innerText = title;
    display_container.appendChild(title_item);

    var jsonString = '{"name": "John", "age": 30, "city": "New York"}';
    var myDict = JSON.parse(display_dct_string);
    console.log(myDict)
    var display_table = document.createElement("table");




    return display_container;
}