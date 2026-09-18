-- Right here there will be the creation of the bindableevents for the disasters 
local meteor_shower = Instance.new("BindableEvent")
meteor_shower.Parent = script
meteor_shower.Name = "1"

local paralimpicous_firing = Instance.new("BindableEvent")
paralimpicous_firing.Parent = script
paralimpicous_firing.Name = "2"

local cooldown = Instance.new("BindableEvent")
cooldown.Parent = script
cooldown.Name= "cooldown"
local cooldown_state = true

local wait_another = Instance.new("BindableEvent")
wait_another.Parent = script
wait_another.Name = "wait_another"

local relations = {
	"meteor_shower",
	"paralimpicous_firing"
}

local n_of_dis = table.getn(relations)
local to_fire
local index
wait_another.Event:Connect(function()
	task.wait(10)
	index = math.random(2, n_of_dis)
	to_fire = script:FindFirstChild(tostring(index))
	to_fire:Fire()
	cooldown:Fire()
end)

local to_exec
local checker

cooldown.Event:Connect(function()
	cooldown_state = false
	to_exec = Instance.new("BoolValue")
	to_exec.Name = "to_exec"
	to_exec.Parent = script
	print("Disaster starting")
	checker = Instance.new("BoolValue")
	checker.Name = "disaster"
	checker.Parent = script
	task.wait(10)
	cooldown_state = true
	print("Disaster ending")
	to_exec:Destroy()
	checker:Destroy()
	wait_another:Fire()
end)


meteor_shower.Event:Connect(function()
	local cur_part
	exec = script:WaitForChild("to_exec")
	local _, __ = pcall(function()
		while not cooldown_state do
			task.wait(0.1)
			cur_part = Instance.new("Part")
			cur_part.Shape = Enum.PartType.Ball
			cur_part.CanCollide = false
			cur_part.Parent = workspace
			cur_part.Size = Vector3.new(30,30,30)
			cur_part.Position = Vector3.new(math.random(0,400), 150, math.random(0,400))
			cur_part.Color = Color3.fromRGB(117, 13, 13)
			cur_part.Material = Enum.Material.Granite
			cur_part.Touched:Connect(function(hit)
				if hit.Parent:FindFirstChildOfClass("Humanoid") then
					hit.Parent:FindFirstChildOfClass("Humanoid"):TakeDamage(100)
				end
			end)
		end
	end)
end)

-- AI SYSTEM

local n_rig
local rig
local pf_humanoid
local pf_line
local weights = {}
local decider
local sum

for count = 0,999,1 do
	local decider = math.random(1,2)
	if decider == 1 then
		table.insert(weights, -math.random(0,1000) / 100)
	else
		table.insert(weights, math.random(0,1000) / 100)
	end
end

local function activation_function()
	for _, weight in weights do
		weight
	end
end

print(weights)

paralimpicous_firing.Event:Connect(function()
	exec = script:WaitForChild("to_exec")
	n_rig = game.ReplicatedStorage.assets:FindFirstChild("pf_rig")
	rig = n_rig:Clone()
	rig.Parent = game.Workspace
	pf_humanoid = rig.Humanoid
	pf_line = game.Workspace.pf_line
	pf_humanoid:MoveTo(pf_line.Position)
	while not cooldown_state do
		pf_humanoid:MoveTo()
	end
end)

wait_another:Fire()



