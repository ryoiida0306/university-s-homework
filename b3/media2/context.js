function context_function(data,name) {
  
  const msg = data.val();    //オブジェクトデータを取得し、変数msgに代入
  const key = data.key;      //データのユニークキー（削除や更新に使用可能）
  const DayTime = msg.year+ "."+msg.month+"/"+msg.date;      //表示用テキスト・HTMLを作成
  const time = msg.hour+":"+msg.minute;
  
  let h = '<div id = uname_'+msg.uname+'>';
      h += msg.uname+"さん";
      h += '</div>';

      h += '<div id = text_'+msg.uname+'>';
      h += msg.text;
      h += '</div>';
      if(msg.uname == name ){
        h += '<div class="midoku">';
        h += "未読";
        h += '</div>';
      }
      h += '<div id = DayTime_'+msg.uname+' >';
      h += DayTime + "  "+time;
      h += '</div>';
      h += '<br>'

  return h;
}



