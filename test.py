import gymnasium as gym

env = gym.make('FrankaKitchen-v1', tasks_to_complete=['microwave', 'kettle'], render_mode='rgb_array') # change the render mode
env = gym.wrappers.RecordVideo(env=env, video_folder="./video", name_prefix="test-video", episode_trigger=lambda x: x % 2 == 0)

observation, info = env.reset()

env.start_video_recorder()

for _ in range(5):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)
    env.render()

    if terminated or truncated:
        observation, info = env.reset()

env.close_video_recorder()

env.close()
