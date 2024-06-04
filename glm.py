import os
from transformers import AutoTokenizer, AutoModel

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

tokenizer = AutoTokenizer.from_pretrained("/Users/wwhm/glm/model/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("/Users/wwhm/glm/model/chatglm2-6b", trust_remote_code=True).to('mps')
# model = AutoModel.from_pretrained("/Users/wwhm/glm/models/chatglm2-6b", trust_remote_code=True).to('mps')
# model = model.eval()
# response, history = model.chat(tokenizer, "你好", history=[])
# print(response)
