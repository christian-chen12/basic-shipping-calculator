p_ground_shipping = 125.00

print('Hello, how much does your package weigh?')
weight = input()

def ground_shipping(weight):
  if weight > 10: 
    return (weight * 4.75) + (20.00)
  elif weight > 6:
    return (weight * 4.00) + (20.00)
  elif weight > 2:
    return (weight * 3.00) + (20.00)
  else:
    return (weight * 1.50) + (20.00)


def drone_shipping(weight):
  if weight > 10:
    return (weight * 14.25)
  elif weight > 6:
    return (weight * 12.00)
  elif weight > 2:
    return (weight * 9.00)
  else:
    return (weight * 4.50)


def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  premium = p_ground_shipping
  drone = drone_shipping(weight)

  if (ground < premium) and (ground < drone):
    print("Ground shipping is the cheapest method and will cost", ground_shipping(weight))
  
  if (premium < ground) and (premium < drone):
    print("Premium Ground shipping is the cheapest method and will cost", p_ground_shipping)
  
  if (drone < ground) and (drone < premium):
    print("Drone shipping is the cheapest method and will cost", drone_shipping(weight))
    
cheapest_shipping(int(weight))
