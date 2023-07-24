from torchbenchmark.tasks import NLP
from torchbenchmark.util.framework.huggingface.model_factory import HuggingFaceModel, HuggingFaceAuthMixin

class Model(HuggingFaceModel, HuggingFaceAuthMixin):
    task = NLP.LANGUAGE_MODELING
    DEFAULT_TRAIN_BSIZE = 1
    DEFAULT_EVAL_BSIZE = 1
    DEEPCOPY = False 

    def __init__(self, test, device, jit=False, batch_size=None, extra_args=[]):
        HuggingFaceAuthMixin.__init__(self)
        super().__init__(name="llama_v2_70b", test=test, device=device, jit=jit, batch_size=batch_size, extra_args=extra_args)

    def train(self):
        return NotImplementedError("70b LLAMA model will OOM on CI GPU machines")

    def eval(self):
        return NotImplementedError("70b LLAMA model will OOM on CI GPU machines")

    def get_module(self):
        return NotImplementedError("70b LLAMA model will OOM on CI GPU machines")

    def fsdp(self):
        # self.model.to(device="meta")
        return NotImplementedError("I haven't figured this out yet!")
