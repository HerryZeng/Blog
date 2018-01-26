// KindEditor.ready(function(K) {
//                  K.create('textarea[name=content]',
//                      {
//                          width:800,
//                          height:400,
//                          uploadJson: '/admin/upload/kindeditor',
//                          uploadJson: ''
//                      });
//
//         });

// KindEditor.ready(function(K) {
//                 K.create('textarea[name=content]',{
//                     width:'800px',
//                     height:'400px',
//                     uploadJson: '/admin/upload/kindeditor',
//                 });
//         });

  KindEditor.ready(function(K) {
    var editor1 = K.create('textarea[name="content"]', {
      uploadJson : '/admin/upload/kindeditor',//dirname为目录名,可留空
      allowFileManager : false,
      afterCreate : function() {
        var self = this;
        K.ctrl(document, 13, function() {
          self.sync();
          K('form[name=example]')[0].submit();
        });
        K.ctrl(self.edit.doc, 13, function() {
          self.sync();
          K('form[name=example]')[0].submit();
        });
      }
    });
  });