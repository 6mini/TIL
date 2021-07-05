function readURL(input) {
    if (input.files && input.files[0]) {
  
      var reader = new FileReader();
  
      reader.onload = function(e) {
        $('.image-upload-wrap').hide();
        $('#loading').show();
        $('.file-upload-image').attr('src', e.target.result);
        $('.file-upload-content').show();
  
        $('.image-title').html(input.files[0].name);
      };
  
      reader.readAsDataURL(input.files[0]);
      init().then(()=>{
        predict();
        $('#loading').hide();
      });
    } else {
      removeUpload();
    }
  }
  
  function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
  }
  $('.image-upload-wrap').bind('dragover', function () {
          $('.image-upload-wrap').addClass('image-dropping');
      });
      $('.image-upload-wrap').bind('dragleave', function () {
          $('.image-upload-wrap').removeClass('image-dropping');
  });
// More API functions here:
// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

// the link to your model provided by Teachable Machine export panel
const URL = "https://teachablemachine.withgoogle.com/models/zU_wz1qit/";

let model, webcam, labelContainer, maxPredictions;

// Load the image model and setup the webcam
async function init() {
    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";

    // load the model and metadata
    // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
    // or files from your local hard drive
    // Note: the pose library adds "tmImage" object to your window (window.tmImage)
    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();



    // append elements to the DOM
    labelContainer = document.getElementById("label-container");
    for (let i = 0; i < maxPredictions; i++) { // and class labels
        labelContainer.appendChild(document.createElement("div"));
    }
}



// run the webcam image through the image model
async function predict() {
    // predict can take in an image, video or canvas html element
    var image = document.getElementById("FasImg")
    const prediction = await model.predict(image, false);
    prediction.sort((a, b) => parseFloat(b.probability) - parseFloat(a.probability));
    var resultTitle, resultExplain, resultCeleb;
    switch (prediction[0].className) {
      case "sexy_feminine":
          resultTitle = "섹시/페미닌룩"
          resultExplain = "다정다감하고 귀여운 당신은 모든 사람들에게 즐거움을 주는 호감형이다! 친절하고 활발한 성격으로 어디에서도 인기폭발이며 애교와 웃음이 많아 연인에게 특히나 사랑스럽다. 당신은 애인바라기로 애인의 관심이 부족하면 시무룩해지고 외로움을 타는 모습이 마치 강아지와 똑 닮았다!"
          resultCeleb = "강아지상 연예인: 강다니엘, 백현(엑소), 박보검, 송중기"
          break;
      case "simple_casual":
          resultTitle = "심플/캐쥬얼룩"
          resultExplain = "무뚝뚝한 당신의 첫인상은 차가워 보이지만 묘한 매력을 풍겨 언제나 인기가 넘친다. 자존심이 세계 1등과 맞먹지만 관심 받는 것을 좋아하고 연인에게는 은근히 애교쟁이다. 시크한 츤데레로 연인에게 끊임없이 설렘을 안겨주는 당신은 고양이와 닮았다!"
          resultCeleb = "고양이상 연예인: 황민현(뉴이스트), 시우민(엑소), 강동원, 이종석, 이준기"
          break;
      case "street_hiphop":
          resultTitle = "스트릿/힙합룩"
          resultExplain = "천진난만하고 귀여운 당신은 주변 사람들에게 기쁨을 주는 행복바이러스다! 호기심이 많아 활발하며 귀엽고 순수한 외모로 연인의 보호본능을 자극한다. 존재 자체가 상큼한 당신은 특별한 애교 없이도 연인에게 너무나도 사랑스럽다!"
          resultCeleb = "토끼상 연예인: 정국(방탄소년단), 바비(아이콘), 박지훈(워너원), 수호(엑소)"
          break;
      case "girlish":
          resultTitle = "걸리시룩"
          resultExplain = "무심한 성격에 첫인상은 나쁜 남자 같지만, 알고 보면 따뜻함이 묻어나는 당신! 시크한 매력에 선뜻 다가가지 못하지만 한번 다가가면 헤어나올 수 없는 터프한 매력을 가진 카리스마 있는 남자다."
          resultCeleb = "공룡상 연예인: 윤두준(하이라이트), 이민기, 김우빈, 육성재(비투비), 공유"
          break;
      case "unique_kitchi":
          resultTitle = "유니크/키치룩"
          resultExplain = "첫 인상은 무서워 보이지만 알고 보면 귀여운 매력의 당신! 꼼꼼하고 섬세한 성격으로 연인을 헌신적으로 챙겨주는 당신은 연인에게 듬직한 존재! 포근한 매력에 듬직함까지 갖춘 최고의 남자다!"
          resultCeleb = "곰상 연예인: 마동석, 조진웅, 조세호, 안재홍"
          break;
      case "formal_classic":
          resultTitle = "포멀/클래식룩"
          resultExplain = "첫 인상은 무서워 보이지만 알고 보면 귀여운 매력의 당신! 꼼꼼하고 섬세한 성격으로 연인을 헌신적으로 챙겨주는 당신은 연인에게 듬직한 존재! 포근한 매력에 듬직함까지 갖춘 최고의 남자다!"
          resultCeleb = "곰상 연예인: 마동석, 조진웅, 조세호, 안재홍"
          break;
      case "work_military":
          resultTitle = "워크/밀리터리룩"
          resultExplain = "첫 인상은 무서워 보이지만 알고 보면 귀여운 매력의 당신! 꼼꼼하고 섬세한 성격으로 연인을 헌신적으로 챙겨주는 당신은 연인에게 듬직한 존재! 포근한 매력에 듬직함까지 갖춘 최고의 남자다!"
          resultCeleb = "곰상 연예인: 마동석, 조진웅, 조세호, 안재홍"
          break;
      default:
          resultTitle = "알수없음"
          resultExplain = ""
          resultCeleb = ""
    }
    var title = "<div class='" + prediction[0].className + "-animal-title'>" + resultTitle + "</div>"
            var explain = "<div class='animal-explain pt-2'>" + resultExplain + "</div>"
            var celeb = "<div class='" + prediction[0].className + "-animal-celeb pt-2 pb-2'>" + resultCeleb + "</div>"
            $('.result-message').html(title + explain + celeb);
            var barWidth;
            for (let i = 0; i < maxPredictions; i++) {
                if (prediction[i].probability.toFixed(2) > 0.1) {
                    barWidth = Math.round(prediction[i].probability.toFixed(2) * 100) + "%";
                } else if (prediction[i].probability.toFixed(2) >= 0.01) {
                    barWidth = "4%"
                } else {
                    barWidth = "2%"
                }
                var labelTitle;
                switch (prediction[i].className) {
                    case "sexy_feminine":
                        labelTitle = "섹시/페미닌룩"
                        break;
                    case "simple_casual":
                        labelTitle = "심플/캐쥬얼룩"
                        break;
                    case "street_hiphop":
                        labelTitle = "스트릿/힙합룩"
                        break;
                    case "girlish":
                        labelTitle = "걸리시룩"
                        break;
                    case "unique_kitchi":
                        labelTitle = "유니크/키치룩"
                        break;
                    case "formal_classic":
                        labelTitle = "포멀/클래식룩"
                        break;
                    case "work_military":
                        labelTitle = "워크/밀리터리룩"
                        break;
                    default:
                        labelTitle = "알수없음"
                }
                var label = "<div class='animal-label d-flex align-items-center'>" + labelTitle + "</div>"
                var bar = "<div class='bar-container position-relative container'><div class='" + prediction[i].className + "-box'></div><div class='d-flex justify-content-center align-items-center " + prediction[i].className + "-bar' style='width: " + barWidth + "'><span class='d-block percent-text'>" + Math.round(prediction[i].probability.toFixed(2) * 100) + "%</span></div></div>"
                labelContainer.childNodes[i].innerHTML = label + bar;
    // for (let i = 0; i < maxPredictions; i++) {
    //     const classPrediction =
    //         prediction[i].className + ": " + prediction[i].probability.toFixed(2);
    //     labelContainer.childNodes[i].innerHTML = classPrediction;
    }
}