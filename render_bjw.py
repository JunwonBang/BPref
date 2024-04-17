import metaworld
import metaworld.envs.mujoco.env_dict as _env_dict
from gym.wrappers.time_limit import TimeLimit
from rlkit.envs.wrappers import NormalizedBoxEnv
from PIL import Image

env_cls = _env_dict.ALL_V2_ENVIRONMENTS['sweep-into-v2']
env = env_cls(render_mode='rgb_array')
_env = TimeLimit(NormalizedBoxEnv(env), env.max_path_length)

obs, _ = _env.reset()

# img_array = _env.render()
# img = Image.fromarray(img_array, 'RGB')
# img = img.save('render_bjw.png')