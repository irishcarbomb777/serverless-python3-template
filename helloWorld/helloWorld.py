from libs.handlerLib import handler
# Run Hello World!

def main(event, context):
  def fn(event, context):
    return "Hello World!"
  return handler(fn(event, context))

if __name__=="__main__":
  main(",", ",")