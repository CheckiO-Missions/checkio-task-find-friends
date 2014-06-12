//Dont change it
requirejs(['ext_editor_1', 'jquery_190', 'raphael_210'],
    function (ext, $, TableComponent) {

        var cur_slide = {};

        ext.set_start_game(function (this_e) {
        });

        ext.set_process_in(function (this_e, data) {
            cur_slide["in"] = data[0];
        });

        ext.set_process_out(function (this_e, data) {
            cur_slide["out"] = data[0];
        });

        ext.set_process_ext(function (this_e, data) {
            cur_slide.ext = data;
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_process_err(function (this_e, data) {
            cur_slide['error'] = data[0];
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_animate_success_slide(function (this_e, options) {
            var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div></div></div>'));
            this_e.setAnimationHeight(115);
        });

        ext.set_animate_slide(function (this_e, data, options) {
            var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
            if (!data) {
                console.log("data is undefined");
                return false;
            }

            var default_in = [
                ["dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
                    "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"],
                "scout2",
                "scout3"
            ];
            var checkioInput = data.in || default_in;
            var chFirst = JSON.stringify(checkioInput[0]).replace(/\[/g, "(").replace(/\]/g, ")");
            if (checkioInput[0].length === 1) {
                chFirst = chFirst.replace(")", ",)");
            }
            var checkioInputStr = ' check_connection(' + chFirst +
                "," + JSON.stringify(checkioInput[1]) + "," + JSON.stringify(checkioInput[2]) + ')';

            var failError = function (dError) {
                $content.find('.call').html('Fail: ' + checkioInputStr);
                $content.find('.output').html(dError.replace(/\n/g, ","));

                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
                $content.find('.answer').remove();
                $content.find('.explanation').remove();
                this_e.setAnimationHeight($content.height() + 60);
            };

            if (data.error) {
                failError(data.error);
                return false;
            }

            if (data.ext && data.ext.inspector_fail) {
                failError(data.ext.inspector_result_addon);
                return false;
            }

            var rightResult = data.ext["answer"];
            var userResult = data.out;
            var result = data.ext["result"];
            var result_addon = data.ext["result_addon"];


            //if you need additional info from tests (if exists)
            var explanation = data.ext["explanation"];

            $content.find('.output').html('&nbsp;Your result:&nbsp;' + JSON.stringify(userResult));

            if (!result) {
                $content.find('.call').html('Fail: ' + checkioInputStr);
                $content.find('.answer').html('Right result:&nbsp;' + JSON.stringify(rightResult));
                $content.find('.answer').addClass('error');
                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
            }
            else {
                $content.find('.call').html('Pass: ' + checkioInputStr);
                $content.find('.answer').remove();
            }
            //Dont change the code before it

            if (explanation) {
                var canvas = new SocialNetwork();
                canvas.draw($content.find(".explanation")[0], explanation, checkioInput[0], checkioInput[1], checkioInput[2]);
            }


            this_e.setAnimationHeight($content.height() + 60);

        });

        //This is for Tryit (but not necessary)
//        var $tryit;
//        ext.set_console_process_ret(function (this_e, ret) {
//            $tryit.find(".checkio-result").html("Result<br>" + ret);
//        });
//
//        ext.set_generate_animation_panel(function (this_e) {
//            $tryit = $(this_e.setHtmlTryIt(ext.get_template('tryit'))).find('.tryit-content');
//            $tryit.find('.bn-check').click(function (e) {
//                e.preventDefault();
//                this_e.sendToConsoleCheckiO("something");
//            });
//        });

        function SocialNetwork(options) {

            var format = Raphael.format;

            //Colors
            var colorOrange4 = "#F0801A";
            var colorOrange3 = "#FA8F00";
            var colorOrange2 = "#FAA600";
            var colorOrange1 = "#FABA00";

            var colorBlue4 = "#294270";
            var colorBlue3 = "#006CA9";
            var colorBlue2 = "#65A1CF";
            var colorBlue1 = "#8FC7ED";

            var colorGrey4 = "#737370";
            var colorGrey3 = "#9D9E9E";
            var colorGrey2 = "#C5C6C6";
            var colorGrey1 = "#EBEDED";

            var colorWhite = "#FFFFFF";

            options = options || {};

            var R = options.radius || 160;
            var objR = 15;
            var w = 25;
            var h = 10;

            var x0 = 10;

            var sizeX = 2 * x0 + 2 * (R + w);
            var sizeY = 2 * x0 + 2 * (R + h);

            var centerX = x0 + R + w;
            var centerY = x0 + R + h;


            var paper;
            var networkObjects = {};

            var attrCircle = {"stroke": colorBlue4, "stroke-width": 2, "fill": colorBlue1};
            var attrRect = {"stroke": colorBlue4, "stroke-width": 2, "fill": colorBlue1};
            var attrNumber = {"font-family": "Robotic, Verdana, Geneva, sans-serif", "font-size": objR * 1.5};
            var attrName = {"font-family": "Robotic, Verdana, Geneva, sans-serif", "font-size": h};
            var attrLine = {"stroke": colorOrange4, "stroke-width": 3};

            this.draw = function(dom, names, network, first, second) {
                paper = Raphael(dom, sizeX, sizeY);
                var angle = Math.PI * 2 / names.length;
                for (var i = 0; i < names.length; i++) {
                    var obj = paper.set();
                    var x = centerX - Math.cos(i * angle) * R;
                    var y = centerY - Math.sin(i * angle) * R;
//                    obj.push(paper.circle(x, y, objR).attr(attrCircle));
                    obj.push(paper.rect(x - w, y - h, 2 * w, 2 * h, h).attr(attrRect));


                    if (names[i] === first || names[i] === second) {
                        obj[0].attr("fill", colorOrange1);
                    }
//                    obj.push(paper.text(x, y, i).attr(attrNumber));
                    obj.push(paper.text(x, y, names[i]).attr(attrName));
                    obj.x = x;
                    obj.y = y;
                    networkObjects[names[i]] = obj;
                }
                for (i = 0; i < network.length; i++) {
                    var connection = network[i].split("-");
                    var fr = networkObjects[connection[0]];
                    var to = networkObjects[connection[1]];
                    paper.path(
                        format("M{0},{1}L{2},{3}",
                            fr.x,
                            fr.y,
                            to.x,
                            to.y)).attr(attrLine).toBack();

                }
            }

        }

        //Your Additional functions or objects inside scope
        //
        //
        //


    }
);
